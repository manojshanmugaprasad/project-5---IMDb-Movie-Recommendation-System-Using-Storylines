import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Header Image
st.image("D:/IMDB project guvi/360_F_527909497_0TeRvfnW7CflXPMH0OoUA3r9woY6Q2Q6.jpg", use_column_width=True)

# Title
st.markdown(
    "<h1 style='text-align: center; color: white;'>IMDb Movie Recommendation System</h1>",
    unsafe_allow_html=True
)

st.write("")

# Load models
tfidf = pickle.load(open("models/tfidf2.pkl", "rb"))
tfidf_matrix = pickle.load(open("models/tfidf_matrix2.pkl", "rb"))
movies = pickle.load(open("models/movies2.pkl", "rb"))

# Recommendation function
def recommend_movies(user_input):
    user_vector = tfidf.transform([user_input])
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)

    scores = list(enumerate(similarity_scores[0]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    top_movies = scores[0:6]
    movie_indices = [i[0] for i in top_movies]

    return movies.iloc[movie_indices]

# UI
st.subheader("Enter Movie Storyline or Few Words")

user_input = st.text_area("Example: wizard magic school boy")

if st.button("Find Movie Recommendations"):

    results = recommend_movies(user_input)

    st.write("---")
    st.subheader("🎯 Exact Match Movie")

    st.success(results.iloc[0]["movie_name"])
    st.write("⭐ Rating:", results.iloc[0]["rating"])
    st.write("📅 Year:", results.iloc[0]["year"])
    st.write("📖 Storyline:", results.iloc[0]["storyline"])

    st.write("---")
    st.subheader("🎬 Similar Movies")

    for i in range(1,6):
        st.info(results.iloc[i]["movie_name"])
        st.write("⭐ Rating:", results.iloc[i]["rating"])
        st.write("📅 Year:", results.iloc[i]["year"])
        st.write("📖 Storyline:", results.iloc[i]["storyline"])
        st.write("------")