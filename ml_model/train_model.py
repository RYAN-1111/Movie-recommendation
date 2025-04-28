import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

import mlflow
import mlflow.sklearn

# Load data
movies = pd.read_csv("data/movies.csv")


# Start MLflow experiment
mlflow.set_experiment("movie_recommendation_experiment")

with mlflow.start_run():

    # Training logic here
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['overview'].fillna(''))
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Log model
    mlflow.sklearn.log_model(tfidf, "tfidf_model")

    # Log metrics (you can later add model evaluation here)
    mlflow.log_metric("num_movies", len(movies))

    # Save locally
    if not os.path.exists('ml_model/models'):
        os.makedirs('ml_model/models')

    with open('ml_model/models/tfidf.pkl', 'wb') as f:
        pickle.dump((tfidf, cosine_sim), f)

    print("Model trained, saved, and logged to MLflow.")
