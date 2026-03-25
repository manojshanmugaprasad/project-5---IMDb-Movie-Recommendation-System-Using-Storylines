**Project Overview**
This project is a Content-Based Movie Recommendation System built using Natural Language Processing (NLP), TF-IDF Vectorization, and Cosine Similarity. The system recommends movies based on storyline similarity. Users can enter a movie storyline in their own words, and the system will identify the exact movie and recommend similar movies.

**Problem Statement**
The goal of this project is to scrape IMDb movie data (movie name and storyline), preprocess the storylines using NLP, and recommend similar movies based on storyline similarity using machine learning techniques.

**Business Use Case**
Recommend movies based on storyline similarity
Help users discover similar movies


**Technologies Used**
Python
Selenium
Pandas
NLP (NLTK)
TF-IDF Vectorizer
Cosine Similarity
Streamlit

**Project Workflow**
Scrape movie data from IMDb using Selenium
Store data in CSV
Preprocess storyline text using NLP
Convert text to vectors using TF-IDF
Calculate similarity using Cosine Similarity
Recommend top 5 similar movies
Display results using Streamlit
