import pandas as pd
import nltk
import requests
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, data_file='final_data.csv', max_features=2000):
        self.data = pd.read_csv(data_file)
        self.ps = PorterStemmer()
        self.cv = CountVectorizer(max_features=max_features, stop_words='english')
        self.vector = None
        self.similarity = None
        self._preprocess_data()

    def _stemming(self, tags):
        y = []
        for i in tags.split():
            y.append(self.ps.stem(i))
        return " ".join(y)

    def _preprocess_data(self):
        self.data['stemmed_tags'] = self.data['tags'].apply(self._stemming)
        self.vector = self.cv.fit_transform(self.data['stemmed_tags']).toarray() 
        self.similarity = cosine_similarity(self.vector)

    def get_movie_titles(self):
        return list(self.data['title'])

    def movies_recommendation(self, title, top_n=5):
        movie_index = self.data[self.data['title'] == title].index[0]
        min_dist = self.similarity[movie_index]
        movie_list = sorted(list(enumerate(min_dist)), reverse=True, key=lambda x: x[1])[1:top_n+1]

        recommended_movies = []
        for i in movie_list:
            recommended_movies.append(self.data.iloc[i[0]]['title'])
        return recommended_movies
    
    def fetch_poster(self, title):
        movie_id = self.data[self.data['title']== title]['movie_id'].values[0]
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8b55e29f167afebdaf2f7d2204e25a4f&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path, poster_path

# Example usage
# recommender = MovieRecommender()
# recommended_movies = recommender.movies_recommendation('Avatar')
# print(recommended_movies)
# full_path = recommender.fetch_poster('Avatar')
# print(full_path)