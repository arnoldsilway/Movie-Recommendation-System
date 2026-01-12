## Movie Recommendation System
The Movie Recommendation System is a user-friendly web application built using Streamlit. It helps users discover new movies similar to ones they already enjoy. By analyzing metadata such as genre, cast, crew, and plot, the system computes similarity scores between movies and recommends the top matches instantly. </br>
</br>

### Technologies & Tools
Here's a quick glance at what powers our recommendation engine:
- **Streamlit** – For building an interactive web UI.
- **Pandas** – For managing movie metadata.
- **Pickle** – For storing preprocessed data and models.
- **Scikit-learn** – To compute cosine similarity between movies.
- **NLTK** – For text cleaning and preprocessing.

### Datasets Used
We use two publicly available datasets from TMDB (The Movie Database):
- `tmdb_5000_movies.csv` – Contains movie titles, overviews, genres, release dates, etc.
- `tmdb_5000_credits.csv` – Contains cast and crew data for the corresponding movies.
These datasets are merged and cleaned to build a comprehensive feature space for our model.


   




