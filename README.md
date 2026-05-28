<p align="left">
<img src="https://img.shields.io/badge/Python-3.10-blue" />
<img src="https://img.shields.io/badge/Framework-Streamlit-red" />
<img src="https://img.shields.io/badge/ML-TF--IDF%20%2B%20Cosine%20Similarity-green" />
<img src="https://img.shields.io/badge/Status-Active-success" />
<img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

<h1 align="center">🎬 Movie Recommendation System</h1>
<p align="center">Content‑based recommender using TF‑IDF + Cosine Similarity</p>

🚀 Executive Summary
This project delivers a content‑based movie recommendation engine that helps users instantly discover films similar to their favorites.
It uses TF‑IDF vectorization and cosine similarity to analyze movie overviews and genres, then recommends the closest matches.

The system includes:

A clean ML pipeline

A reusable recommendation engine

A Streamlit UI for interactive exploration

Visual insights into genres, release trends, and similarity scores

This is a portfolio‑grade ML engineering project demonstrating data preprocessing, feature engineering, model artifact creation, and UI deployment.

🎯 Problem Statement
Streaming platforms host tens of thousands of movies, overwhelming users with choice.
Traditional search is not enough — users want personalized, similarity‑based discovery.

User pain points:
Too many options → decision fatigue

Hard to find movies similar to what they already like

Genre filters are too broad

Manual browsing wastes time

This project solves:
Automatic similarity‑based recommendations

Faster content discovery

Personalized exploration

A transparent, explainable ML approach

📈 Business Impact (Quantified)
Content‑based recommenders like this one drive measurable improvements in engagement.

Industry benchmarks show:

20–35% increase in user engagement

15–25% increase in watch‑time

10–20% reduction in churn

Higher satisfaction due to personalized discovery

For a platform with 1M monthly users, even a 5% lift in engagement yields:

50,000 more active users

Millions in additional revenue (ads, retention, subscriptions)

This project demonstrates the core engine behind such systems.

🧠 How the Model Works
1️⃣ Data Preparation
Parse genres

Clean text

Combine overview + genres

2️⃣ Feature Engineering
TF‑IDF vectorization

Sparse matrix representation

Cosine similarity computation

3️⃣ Recommendation Engine
Given a movie title:

Retrieve its vector

Compute similarity with all movies

Return top‑N similar titles

4️⃣ Interactive UI
Streamlit app for real‑time recommendations

Visualizations for transparency

Explore the architecture:

Model Pipeline

Similarity Computation

🏗️ Architecture Overview
┌──────────────────────────┐
│      movies.csv          │
│   (raw movie metadata)   │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   notebook.ipynb         │
│  - text cleaning          │
│  - TF-IDF vectorization   │
│  - cosine similarity      │
│  - save artifacts         │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     recommender.py       │
│  - load artifacts         │
│  - recommend(title, n)    │
└───────┬─────────┬────────┘
        │         │
        ▼         ▼
┌────────────┐   ┌────────────────┐
│ Streamlit  │   │   FastAPI      │
│   app.py   │   │    api.py      │
│ UI client  │   │ REST endpoint  │
└────────────┘   └────────────────┘

📊 Visualizations Included
Genre Distribution

Movies Released per Year

Wordcloud of Movie Overviews

Similarity Score Chart

These help stakeholders understand dataset patterns and model behavior.

🧪 Example Recommendation Output: 
Input: "Inception"

Top Recommendations:
- Interstellar
- Shutter Island
- The Prestige
- Source Code
- The Dark Knight Rises

🛠️ Tech Stack
Python 3.10
Pandas, NumPy
Scikit‑learn (TF‑IDF + Cosine Similarity)
Streamlit
FastAPI
Pickle for model artifacts

🚀 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/<your-username>/movie-recommender.git
cd movie-recommender
2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the Streamlit app
streamlit run src/app.py
Note: App will open at: http://localhost:8501
5️⃣ (Optional) Run the FastAPI backend
uvicorn src.api:app --reload
Note: API docs available at:http://127.0.0.1:8000/docs

📂 Project Structure
movie-recommender/
│── data/
│   └── movies.csv
│── src/
│   ├── app.py
│   ├── api.py
│   └── recommender.py
│── notebook.ipynb
│── processed_movies.csv
│── tfidf.pkl
│── similarity.pkl
│── requirements.txt
│── README.md

🔮 Future Enhancements
Upgrade to BERT embeddings
Add FAISS vector search for scalability
Add user‑based collaborative filtering
Deploy Streamlit app to Streamlit Cloud
Deploy FastAPI to Render / Azure

Explore enhancements:
Add FAISS
Upgrade to BERT

