from flask import Flask, request, render_template
from movie_recommender import MovieRecommender

app = Flask(__name__)

# Initialize movie recommender
recommender = MovieRecommender()

@app.route('/', methods=['GET'])
def index():
    movie_titles = recommender.get_movie_titles()
    if request.method == 'GET':
        title = request.args.get('title')
        if title:
            recommended_movies = recommender.movies_recommendation(title)
            selected_poster, _ = recommender.fetch_poster(title)
            recommended_movies_with_poster = []
            for movie in recommended_movies:
                poster_url, _ = recommender.fetch_poster(movie)
                recommended_movies_with_poster.append((movie, poster_url))
            return render_template('index.html',  movie_titles=movie_titles, recommended_movies=recommended_movies_with_poster, selected_poster=selected_poster)
        
    return render_template('index.html', movie_titles=movie_titles)


if __name__ == '__main__':
    app.run(debug=True)
