from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load data
movies = pd.read_csv("data/movies.csv")

# Load model
with open("ml_model/models/tfidf.pkl", "rb") as f:
    tfidf, cosine_sim = pickle.load(f)

# Function to recommend movies
def recommend(movie_title, top_n=5):
    idx = movies[movies['title'].str.lower() == movie_title.lower()].index
    if len(idx) == 0:
        return []
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:top_n+1]]
    return movies['title'].iloc[movie_indices].tolist()

# API endpoint
@app.get("/recommend")
def get_recommendations(movie: str):
    recommended_movies = recommend(movie)
    return {"recommended_movies": recommended_movies}
