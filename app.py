import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import google.generativeai as genai

# ======================================
# 🔹 Configure Google Generative AI
# ======================================

API_KEY = "AIzaSyA16qj1Ob4VAMdER0hXTTIUJC0od6_ZcNk"  
genai.configure(api_key=API_KEY)

# ✅ Use a valid Gemini model name
# Options: "gemini-2.0-flash", "gemini-2.0-pro", "gemini-2.5-flash", "gemini-2.5-pro"
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# ======================================
# 🔹 Movie Recommendation System Setup
# ======================================

# Load movie data
with open('movies_dict.pkl', 'rb') as file:
    movies_dict = pickle.load(file)
movies = pd.DataFrame(movies_dict)

# Load similarity data
with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

# ======================================
# 🔹 Functions
# ======================================

def recommend(movie):
    """Recommend top 5 similar movies."""
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies


def search_actor_or_movie(input_text, search_type):
    """Use Gemini to fetch movie or actor details."""
    if search_type == "Actor":
        prompt = (
            f"Provide short, clear details for actor '{input_text}':\n"
            f"- Full name\n- Birthdate (if known)\n- Top movies worked in\n"
            f"- Awards or recognitions (if any)\n- Short summary"
        )
    else:
        prompt = (
            f"Provide a brief, clear summary for the movie '{input_text}':\n"
            f"- Release date\n- Director\n- Cast\n- Genre or theme\n- Short description"
        )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error while contacting Gemini API: {str(e)}"

# ======================================
# 🔹 Streamlit UI Setup
# ======================================

st.set_page_config(
    page_title="Entertainment Insights",
    page_icon="🎬",
    layout="wide"
)

# ======================================
# 🔹 Navigation Menu
# ======================================

selected = option_menu(
    menu_title=None,
    options=["Movie Recommendations", "Actor and Movie Search"],
    icons=["film", "search"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "blue", "font-size": "25px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "3px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#2c3e50"},
    }
)

# ======================================
# 🔹 Movie Recommendation Page
# ======================================

if selected == "Movie Recommendations":
    st.markdown("<h1 style='text-align: center;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.text("Looking for your next great watch? Select a movie, and we’ll recommend similar films you might enjoy 🍿")
        selected_movie_name = st.selectbox(
            "Select a movie:",
            movies['title'].values,
            key="movie_select",
        )
        if st.button("Recommend", key="recommend"):
            recommendations = recommend(selected_movie_name)
            st.subheader("Recommended Movies:")
            for movie in recommendations:
                st.write(f"🎬 {movie}")

# ======================================
# 🔹 Actor and Movie Search Page
# ======================================

elif selected == "Actor and Movie Search":
    st.markdown("<h1 style='text-align: center;'>🔍 Actor & Movie Search</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tabs = st.tabs(["Actors", "Movies"])

        # --- Actor Search ---
        with tabs[0]:
            st.subheader("Search for an Actor")
            actor_query = st.text_input("Enter Actor Name:", key="actor_search_input")
            if st.button("Search Actor", key="actor_search"):
                if actor_query:
                    result = search_actor_or_movie(actor_query, "Actor")
                    st.subheader("Search Results:")
                    st.write(result)
                else:
                    st.warning("Please enter a valid actor name.")

        # --- Movie Search ---
        with tabs[1]:
            st.subheader("Search for a Movie")
            movie_query = st.text_input("Enter Movie Name:", key="movie_search_input")
            if st.button("Search Movie", key="movie_search"):
                if movie_query:
                    result = search_actor_or_movie(movie_query, "Movie")
                    st.subheader("Search Results:")
                    st.write(result)
                else:
                    st.warning("Please enter a valid movie name.")
