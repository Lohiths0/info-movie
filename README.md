A webpage to display information related to movies

Prerequisites to run the script:

  1. flask; pip install Flask
  2. request; pip install request
  3. requests; pip install requests
  4. JSON

In order to run the script, run the backend.py file and navigate to http://127.0.0.1:5000/ (localhost) and input the name of the movie into the search box and hit 'submit'.

The script will render another HTML page with the movie's

  1. ratings (IMDB, Metacritic, and rotten tomatoes)
  2. plot summary
  3. embedded video of the movie's trailer
  4. 3 (unformatted) reviews

APIs used-
OMDB (Open Movie Database) for Plot; Ratings (IMDB, Metacritic, and rotten tomatoes), and IMDB ID
TMDB (The Movie Database) for Reviews, Movie Trailer (Embedded youtube video)

