import ast
import pandas as pd
import requests
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

TMDB_API_KEY = "7b995d3c6fd91a2284b4ad8cb390c7b8"


def parse_names(value, limit=None):
    if not isinstance(value, str):
        return []
    try:
        items = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return []

    names = []
    source = items[:limit] if limit else items
    for item in source:
        if isinstance(item, dict):
            name = item.get("name")
            if name:
                names.append(name.replace(" ", ""))
    return names


def parse_director(value):
    if not isinstance(value, str):
        return []
    try:
        items = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return []

    for item in items:
        if isinstance(item, dict) and item.get("job") == "Director":
            name = item.get("name")
            return [name.replace(" ", "")] if name else []
    return []


@st.cache_resource(show_spinner="Preparing movie data...")
def load_data():
    movies = pd.read_csv("tmdb_5000_movies.csv")
    credits = pd.read_csv("tmdb_5000_credits.csv")

    movies = movies[["id", "title", "overview", "genres", "keywords"]].copy()
    credits = credits[["movie_id", "cast", "crew"]].copy()

    data = movies.merge(
        credits,
        left_on="id",
        right_on="movie_id",
        how="inner"
    )

    data["overview"] = data["overview"].fillna("").astype(str)
    data["genres"] = data["genres"].apply(parse_names)
    data["keywords"] = data["keywords"].apply(parse_names)
    data["cast"] = data["cast"].apply(lambda x: parse_names(x, limit=3))
    data["crew"] = data["crew"].apply(parse_director)

    data["tags"] = (
        data["overview"]
        + " " + data["genres"].apply(" ".join)
        + " " + data["keywords"].apply(" ".join)
        + " " + data["cast"].apply(" ".join)
        + " " + data["crew"].apply(" ".join)
    ).str.lower()

    data = data[["id", "title", "tags"]].reset_index(drop=True)

    vectorizer = CountVectorizer(
        max_features=5000,
        stop_words="english"
    )
    vectors = vectorizer.fit_transform(data["tags"].astype(str))

    return data, vectors


def recommend(title, data, vectors, count=10):
    matches = data.index[
        data["title"].astype(str) == str(title)
    ].tolist()

    if not matches:
        return pd.DataFrame(columns=["id", "title"])

    movie_index = matches[0]

    scores = cosine_similarity(
        vectors[movie_index],
        vectors
    ).ravel()

    ranked = scores.argsort()[::-1]
    ranked = [i for i in ranked if i != movie_index][:count]

    return data.iloc[ranked][["id", "title"]].reset_index(drop=True)


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{int(movie_id)}"
        response = requests.get(
            url,
            params={"api_key": TMDB_API_KEY},
            timeout=8
        )

        if response.status_code != 200:
            return None

        poster_path = response.json().get("poster_path")

        if not poster_path:
            return None

        return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except Exception:
        return None


st.title("🎬 Movie Recommendation System")
st.write("Choose a movie and get 10 similar movie recommendations with posters.")

try:
    movies, vectors = load_data()

except FileNotFoundError as exc:
    st.error(f"Required CSV file is missing: {exc.filename}")
    st.stop()

except Exception as exc:
    st.error(f"Could not prepare movie data: {exc}")
    st.stop()


selected_movie = st.selectbox(
    "Select a movie",
    movies["title"].astype(str).tolist()
)


if st.button("🎯 Recommend Movies"):

    recommendations = recommend(
        selected_movie,
        movies,
        vectors
    )

    if recommendations.empty:
        st.warning("No recommendations found for this movie.")

    else:
        st.subheader(
            f"Movies similar to {selected_movie}"
        )

        for row_start in range(0, len(recommendations), 5):
            cols = st.columns(5)

            batch = recommendations.iloc[
                row_start:row_start + 5
            ]

            for col, (_, movie) in zip(cols, batch.iterrows()):
                with col:
                    poster = fetch_poster(movie["id"])

                    if poster:
                        st.image(
                            poster,
                            use_container_width=True
                        )
                    else:
                        st.info("Poster unavailable")

                    st.markdown(
                        f"**{movie['title']}**"
                    )
