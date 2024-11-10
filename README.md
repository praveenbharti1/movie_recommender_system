## Movie Recommender System

This project implements a simple movie recommender system using Python, NLTK, and Pandas. The recommendation system is based on the **TMDB 5000 Movie Dataset**, which contains information about 5000 movies.

### Types of Recommender Systems

1. **Demographic Filtering**:
   - Offers generalized recommendations based on movie popularity and genre.
   - Recommends the same movies to users with similar demographic features.
   - Assumes that popular and critically acclaimed movies are likely to be liked by the average audience.

2. **Content-Based Filtering**:
   - Suggests similar items based on a specific item's metadata (e.g., genre, director, description, actors).
   - If a user liked a particular movie, they are likely to enjoy similar movies.

3. **Collaborative Filtering**:
   - Matches users with similar interests and provides recommendations based on this matching.
   - Does not require item metadata.
   - Used by platforms like Amazon and Netflix.

### Dataset

We use two datasets:
1. **tmdb_5000_credits.csv**:
   - Contains features such as movie ID, cast (lead and supporting actors), and crew (director, editor, composer, writer, etc.).

2. **tmdb_5000_movies.csv**:
   - Includes features like movie ID, title, overview, release date, budget, revenue, genres, and keywords.

### Approach

Our recommender system combines metadata from the cast, crew, and keywords to make recommendations. Specifically, we extract the three most important actors, the director, and relevant keywords associated with each movie.

![image](https://github.com/user-attachments/assets/516bf0a9-45ed-49b8-b8dc-20448fa89cc4)



![image](https://github.com/user-attachments/assets/c9a73f88-25b6-4627-9411-9ac1bfd8ad23)



### Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/praveenbharti1/movie_recommender_system.git
   ```

2. Install the required dependencies:
   - Python 3.x
   - Pandas
   - NumPy
   - scikit-learn
   - NLTK
   - Streamlit (for local deployment)

### Usage

1. Explore the dataset and preprocess the data.
2. Implement different recommendation engines (e.g., simple recommender, content-based, collaborative filtering, hybrid engine).
3. Evaluate and fine-tune your recommender system.

Feel free to contribute and enhance this project! 🎬🍿

For more details, check out the [GitHub repository](https://github.com/praveenbharti1/movie_recommender_system).

---
