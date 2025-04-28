import requests
import pandas as pd

API_KEY = "fd30e4db582d841f5a76052b1c49eff4"

def fetch_popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    movies = response.json().get('results', [])
    movie_list = []
    for movie in movies:
        movie_list.append({
            'id': movie['id'],
            'title': movie['title'],
            'overview': movie['overview'],
            'popularity': movie['popularity'],
            'vote_average': movie['vote_average']
        })
    return pd.DataFrame(movie_list)

if __name__ == "__main__":
    df = fetch_popular_movies()
    df.to_csv("data/movies.csv", index=False)
    print("Saved movies to data/movies.csv")
