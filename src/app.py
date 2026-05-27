import streamlit as st
import pandas as pd
import pickle

# Load artifacts
df = pd.read_csv("processed_movies.csv")

with open("tfidf.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

# Recommendation function
def recommend(title, n=5):
    if title not in df['title'].values:
        return []

    idx = df[df['title'] == title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]
    return [df.iloc[i[0]]['title'] for i in scores]

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorite film!")

movie_list = df['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    recs = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for r in recs:
        st.write(f"- {r}")
