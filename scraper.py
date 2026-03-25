import time
import pandas as pd
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

os.makedirs("data/raw", exist_ok=True)

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31"
driver.get(url)

time.sleep(5)

# Scroll to load movies
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

movies = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

movie_names = []
genres = []
ratings = []
years = []
storylines = []

for movie in movies:

    # Title
    try:
        title = movie.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text
    except:
        title = "NA"

    # Genre
    try:
        genre = movie.find_element(By.CSS_SELECTOR, "span.ipc-chip__text").text
    except:
        genre = "NA"

    # Rating
    try:
        rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text
    except:
        rating = "0"

    # Year
    try:
        year = movie.find_element(By.CSS_SELECTOR, "span.sc-300a8231-7").text
    except:
        year = "2024"

    # Storyline
    try:
        storyline = movie.find_element(By.CSS_SELECTOR, "div.ipc-html-content-inner-div").text
    except:
        storyline = "NA"

    movie_names.append(title)
    genres.append(genre)
    ratings.append(rating)
    years.append(year)
    storylines.append(storyline)

driver.quit()

df = pd.DataFrame({
    "movie_name": movie_names,
    "genre": genres,
    "rating": ratings,
    "year": years,
    "storyline": storylines
})

print("Movies scraped:", len(df))

df.to_csv("imdb_movies_2024.csv", index=False)

print("CSV saved successfully")