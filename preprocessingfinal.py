import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Load data
df = pd.read_csv("data/raw/imdb_movies_2024.csv")

# Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = word_tokenize(text)
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)

# Clean storyline
df["cleaned_storyline"] = df["storyline"].apply(clean_text)

# 🔴 IMPORTANT LINE — ADD HERE
df["combined_features"] = df["movie_name"] + " " + df["cleaned_storyline"]

# TF-IDF
tfidf = TfidfVectorizer(ngram_range=(1,2))
tfidf_matrix = tfidf.fit_transform(df["combined_features"])

# Save models
pickle.dump(tfidf, open("models/tfidf2.pkl", "wb"))
pickle.dump(tfidf_matrix, open("models/tfidf_matrix2.pkl", "wb"))
pickle.dump(df, open("models/movies2.pkl", "wb"))

print("Preprocessing completed and models saved.")