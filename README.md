# 🎬 Movie Recommendation System (Content-Based)

## 📌 Overview
A simple but powerful movie recommendation system using TF-IDF and cosine similarity.  
Given a movie title, the system returns the top similar movies based on plot and genre.

## 🚀 Tech Stack
- Python
- pandas
- scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## 📂 Project Structure
movie-recommender/
│── data/
│── src/
│── notebook.ipynb
│── requirements.txt
│── README.md

## 🧠 How It Works
1. Load movie metadata (title, overview, genres)
2. Combine text fields into a single feature
3. Convert text into TF-IDF vectors
4. Compute cosine similarity between all movies
5. Recommend top N similar movies

## ▶️ Running the Project
