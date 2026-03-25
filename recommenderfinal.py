import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

tfidf = pickle.load(open("models/tfidf.pkl", "rb"))
tfidf_matrix = pickle.load(open("models/tfidf_matrix.pkl", "rb"))
movies = pickle.load(open("models/movies.pkl", "rb"))

def recommend_movies(user_input):

    user_vector = tfidf.transform([user_input])

    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)

    scores = list(enumerate(similarity_scores[0]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    top_movies = scores[0:6]

    movie_indices = [i[0] for i in top_movies]

    return movies.iloc[movie_indices]