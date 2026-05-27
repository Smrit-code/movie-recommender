import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, df):
        self.df = df
        self.df['combined'] = (
            df['overview'].fillna('') + ' ' +
            df['genres'].fillna('')
        )

        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['combined'])
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def recommend(self, title, n=5):
        if title not in self.df['title'].values:
            return f"Movie '{title}' not found."

        idx = self.df[self.df['title'] == title].index[0]
        scores = list(enumerate(self.similarity_matrix[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]

        recommendations = [self.df.iloc[i[0]]['title'] for i in scores]
        return recommendations
