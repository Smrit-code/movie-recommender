from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI(title="Movie Recommender API")

# Load artifacts
df = pd.read_csv("processed_movies.csv")

with open("tfidf.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

def recommend(title, n=5):
    if title not in df['title'].values:
        return []

    idx = df[df['title'] == title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]
    return [df.iloc[i[0]]['title'] for i in scores]

@app.get("/recommend")
def recommend_api(title: str, n: int = 5):
    return {"input": title, "recommendations": recommend(title, n)}
