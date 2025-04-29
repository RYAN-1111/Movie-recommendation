import requests
import pandas as pd

API_KEY = ""

def fetch_popular_movies(pages=500):  # specify how many pages you want
    movie_list = []
    for page in range(1, pages + 1):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
        response = requests.get(url)
        if response.status_code == 200:
            movies = response.json().get('results', [])
            for movie in movies:
                movie_list.append({
                    'id': movie['id'],
                    'title': movie['title'],
                    'overview': movie['overview'],
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average']
                })
        else:
            print(f"Failed to fetch page {page}: {response.status_code}")
            break
    return pd.DataFrame(movie_list)

if __name__ == "__main__":
    df = fetch_popular_movies()  
    df.to_csv("data/movies.csv", index=False)
    print(f"Saved {len(df)} movies to data/movies.csv")
