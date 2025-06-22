# Import necessary modules
from flask import Flask, render_template, request
import requests
import os

# Initialize the Flask app
app = Flask(__name__)

# Get TMDB API key from environment variable, fallback to default if not set
API_KEY = os.getenv("TMDB_API_KEY", "04c36cfb275a6f951e9c16651d27ea18")

# Base URL for TMDB API to fetch movies
TMDB_BASE_URL = "https://api.themoviedb.org/3/discover/movie"

# Function to fetch top 3 movies in a given language
def fetch_movies(language):
    params = {
        "api_key": API_KEY,
        "language": language,
        "sort_by": "popularity.desc"
    }
    # Make GET request to TMDB API
    response = requests.get(TMDB_BASE_URL, params=params)

    # If successful, return top 3 movies
    if response.status_code == 200:
        return response.json().get("results", [])[:3]
    
    # If error, return empty list
    return []

# Route for homepage – just shows buttons
@app.route("/")
def home():
    return render_template("index.html")

# Route for /movies – triggered by button click form (POST method)
@app.route("/movies", methods=["POST"])
def movies():
    lang = request.form.get("language")  # 'hindi' or 'english'

    # Convert to TMDB-supported language codes
    if lang == "hindi":
        language_code = "hi-IN"
    else:
        language_code = "en-US"

    # Fetch movies from TMDB API
    movie_data = fetch_movies(language_code)

    # Render template with movie data and selected language
    return render_template("index.html", movies=movie_data, lang=lang)

# Run the Flask app (on 0.0.0.0 for Docker, port 5000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
