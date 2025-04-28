import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Load data
movies = pd.read_csv("data/movies.csv")

# Feature Extraction
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'].fillna(''))

# Similarity Matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save model
if not os.path.exists('ml_model/models'):
    os.makedirs('ml_model/models')

with open('ml_model/models/tfidf.pkl', 'wb') as f:
    pickle.dump((tfidf, cosine_sim), f)

print("Model trained and saved to ml_model/models/tfidf.pkl")
