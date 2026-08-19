# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using Python, Machine Learning, and Streamlit. The application recommends **10 similar movies** based on the movie selected by the user and displays their posters using the **TMDB API**.

## 📌 Overview

This project helps users discover movies similar to their favorite movies.

The recommendation system analyzes movie information such as:

* Overview
* Genres
* Keywords
* Cast
* Director

These features are converted into numerical vectors using **CountVectorizer**, and **Cosine Similarity** is used to identify movies with similar content.

The application is built using **Streamlit**, which provides a simple and interactive web interface.

## ✨ Features

* 🎬 Select a movie from the dropdown
* 🤖 Get Top 10 similar movie recommendations
* 🖼️ Display movie posters
* 🔍 Content-based recommendation system
* 📊 Uses Cosine Similarity
* 🌐 Interactive Streamlit web application
* 🎞️ Movie posters fetched using TMDB API

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* CountVectorizer
* Cosine Similarity
* TMDB API
* Requests

## 📂 Dataset

The project uses the **TMDB 5000 Movie Dataset**.

Main dataset files:

```text
tmdb_5000_movies.csv
tmdb_5000_credits.csv
```

Dataset:

[TMDB Movie Metadata – Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## ⚙️ How It Works

1. Load movie and credits datasets.
2. Merge both datasets using movie IDs.
3. Extract important movie features such as genres, keywords, cast, director, and overview.
4. Combine these features into a single `tags` column.
5. Convert movie tags into vectors using **CountVectorizer**.
6. Calculate similarity between movies using **Cosine Similarity**.
7. Select the movies with the highest similarity scores.
8. Display the Top 10 recommended movies.
9. Fetch and display movie posters using the **TMDB API**.

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rupasreesurapaneni777/Movie-Recommendation-System.git
```

### 2. Open the project folder

```bash
cd Movie-Recommendation-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install required packages

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install streamlit pandas scikit-learn requests
```

## ▶️ Run the Application

Run:

```bash
python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

in your browser.

## 🖥️ Output

The user selects a movie from the dropdown and clicks **Recommend Movies**.

The system displays the **Top 10 similar movies along with their posters**.

### Example: Avatar Recommendations

![Movie Recommendation System Output](output.png)

The application successfully recommends movies similar to the selected movie using content-based filtering and cosine similarity.

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── Movie_Recommendation_System.ipynb
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── output.png
├── README.md
└── .gitignore
```

## 🧠 Machine Learning Technique

### Content-Based Filtering

The recommendation engine uses **Content-Based Filtering**.

It recommends movies based on similarities between movie features rather than user ratings.

### CountVectorizer

CountVectorizer converts movie information into numerical feature vectors.

### Cosine Similarity

Cosine Similarity measures how similar two movie vectors are.

Movies with higher similarity scores are selected as recommendations.

## 📊 Result

The Movie Recommendation System successfully:

* Processes movie metadata
* Finds similar movies
* Generates Top 10 recommendations
* Displays movie posters
* Provides an interactive web interface

## 🔮 Future Improvements

* Add movie ratings
* Add movie descriptions
* Add release year and genres
* Add trailer links
* Improve movie search
* Add collaborative filtering
* Deploy the application online

## 📚 References

* [TMDB Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* [YouTube Tutorial](https://youtu.be/i-B_I2DGIAI)

## 📄 License

This project is licensed under the **MIT License**.
