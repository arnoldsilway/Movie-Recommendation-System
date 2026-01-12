## Movie Recommendation System
The Movie Recommendation System is a user-friendly web application built using Streamlit. It helps users discover new movies similar to ones they already enjoy. By analyzing metadata such as genre, cast, crew, and plot, the system computes similarity scores between movies and recommends the top matches instantly. </br>
</br>

Movie-Recommendation-System/
│
├── app.py                         # Main Streamlit application (UI entry point)
│
├── data/                          # Dataset storage
│   ├── movies.csv                 # Movie metadata dataset
│   ├── credits.csv                # Cast & crew information
│   └── processed_movies.csv       # Cleaned & merged dataset
│
├── models/                        # Saved models & similarity files
│   ├── similarity.pkl             # Cosine similarity matrix
│   └── movies.pkl                 # Processed movie objects
│
├── notebooks/                     # Jupyter notebooks (experimentation)
│   ├── data_preprocessing.ipynb   # Data cleaning & feature engineering
│   └── model_building.ipynb       # Recommendation logic & similarity creation
│
├── src/                           # Core logic and helper modules
│   ├── __init__.py
│   ├── recommender.py             # Recommendation algorithm logic
│   ├── preprocessing.py           # Data preprocessing functions
│   └── utils.py                   # Helper functions
│
├── assets/                        # Static assets
│   └── screenshots/               # App screenshots for README
│
├── requirements.txt               # Project dependencies
│
├── README.md                      # Project documentation
│
├── LICENSE                        # License file (MIT / Apache etc.)
│
└── .gitignore                     # Ignored files & folders





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

### Working of Project
1. **Loading and Merging Datasets:** The TMDB datasets (tmdb_5000_movies.csv and tmdb_5000_credits.csv) are loaded and merged based on the movie_id to create a unified dataframe.
2. **Text Preprocessing & Feature Engineering:** We combine columns such as genre, cast, director, and overview into a unified text field.
3. **Calculating Similarity:** We use cosine similarity to measure how close two movies are:

    ```python
    from sklearn.metrics.pairwise import cosine_similarity
    similarity = cosine_similarity(vectors)
    ```
4. **Fast Retrieval with Pickle:** To avoid recomputation, we serialize the movie dictionary and similarity matrix using `.pkl` files.

   ```python
   with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)
   ```
#### Frontend(app.py)
5. **Movie Recommendation Tab** : Loads the pickled files then, provides a dropdown for movie selection and displays top 5 similar movies using a recommend function:
 ```python
  def recommend(movie):
      movie_index = movies[movies['title'] == movie].index[0]
      distances = similarity[movie_index]
      movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
      return [movies.iloc[i[0]].title for i in movies_list]
   ```
6. At last, we have the **Actor and Movie Search Tab**, which allows users to input any movie or actor name and receive structured information in return. </br>
    📽️ For movies: title, release date, director, genre, cast, and a short description. </br>
    🎭 For actors: full name, birthdate, and notable filmography. </br>
    It’s an intelligent assistant built right into the app, making movie exploration more insightful and engaging.

