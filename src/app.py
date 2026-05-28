import streamlit as st
import pandas as pd
import pickle
import altair as alt
import ast

# ==========================
# 📌 Load Data & Artifacts
# ==========================

df = pd.read_csv("processed_movies.csv")

with open("tfidf.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

# Parse genres for charts
# Parse genres (already saved as list of strings in processed_movies.csv)
df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x))
df['genres_str'] = df['genres'].apply(lambda x: " ".join(x))

# Release year (if available)
if "release_date" in df.columns:
    df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year


# ==========================
# 🎯 Recommendation Function
# ==========================

def recommend(title, n=5):
    if title not in df['title'].values:
        return [], []

    idx = df[df['title'] == title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]

    recommended_titles = [df.iloc[i[0]]['title'] for i in scores]
    recommended_scores = [i[1] for i in scores]

    return recommended_titles, recommended_scores


# ==========================
# 🎬 Streamlit UI
# ==========================

st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorite film!")

# Sidebar for visualizations
st.sidebar.header("📊 Data Visualizations")

viz_option = st.sidebar.selectbox(
    "Choose a visualization",
    [
        "Genre Distribution",
        "Movies Released per Year",
        "Similarity Scores (after recommendation)"
    ]
)

# ==========================
# 📊 Visualization Section
# ==========================

if viz_option == "Genre Distribution":
    st.subheader("🎭 Genre Distribution")

    genre_counts = df['genres_str'].str.split().explode().value_counts().reset_index()
    genre_counts.columns = ['genre', 'count']

    chart = alt.Chart(genre_counts).mark_bar().encode(
        x='count',
        y=alt.Y('genre', sort='-x')
    )

    st.altair_chart(chart, use_container_width=True)


elif viz_option == "Movies Released per Year":
    st.subheader("📈 Movies Released per Year")

    if "release_year" in df.columns:
        year_counts = df['release_year'].value_counts().sort_index().reset_index()
        year_counts.columns = ['year', 'count']

        st.line_chart(year_counts.set_index("year"))
    else:
        st.warning("Release year data not available in processed_movies.csv")


elif viz_option == "Similarity Scores (after recommendation)":
    st.subheader("🎯 Similarity Scores")
    st.info("Run a recommendation first to see similarity scores.")


# ==========================
# 🎥 Recommendation Section
# ==========================

movie_list = df['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    recommended_titles, recommended_scores = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for r in recommended_titles:
        st.write(f"- {r}")

    # Show similarity score chart
    if recommended_titles:
        scores_df = pd.DataFrame({
            "Movie": recommended_titles,
            "Similarity": recommended_scores
        })

        st.subheader("🔍 Similarity Score Chart")
        st.bar_chart(scores_df.set_index("Movie"))
