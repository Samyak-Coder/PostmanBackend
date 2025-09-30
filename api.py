import requests # type: ignore 
from flask import Flask, render_template, request, redirect, url_for # type: ignore 
import random
import os
from dotenv import load_dotenv #type: ignore

load_dotenv()

app = Flask(__name__)

OMDB_API_KEY = os.getenv('API_KEY')
OMDB_BASE_URL = "http://www.omdbapi.com/"

@app.route('/api/movie/title', methods = ['GET'])
def get_movie_details():
    title = request.args.get('title')
    params = {
        't': title,
        'apikey': OMDB_API_KEY,
        'plot': 'short'
    }
    
    try:
        response = requests.get(OMDB_BASE_URL, params=params)
        response.raise_for_status() 
        data = response.json()
        
        if data.get('Response') == 'True':
            
            movie_details = {
                'Title': data.get('Title', 'N/A'),
                'imdbID': data.get('imdbID'),
                'Year': data.get('Year', 'N/A'),
                'Genre': data.get('Genre', 'N/A'),
                'Director': data.get('Director', 'N/A'),
                'imdbRating': data.get('imdbRating', 0),
                'Plot': data.get('Plot', 'N/A') 
            }
            # print(movie_details)
            return movie_details
        else:
           
            return {"Error": data.get('Error', 'Movie not found.')}
            
    except requests.exceptions.RequestException as e:
        return {"Error": f"An error occurred while connecting to OMDb: {e}"}
    
#series
@app.route('/api/series', methods = ['GET'])
def get_series_details():
    
    sTitle = request.args.get('t')
    sNumber = request.args.get('Season')
    epNumber = request.args.get('episode')
    
    params = {
        'type': 'series',
        'apikey': OMDB_API_KEY,
        'episode': epNumber,
        'Season': sNumber,
        't': sTitle,
        'plot': 'short',
        
    }
    
    try:
        response = request.args.get(OMDB_BASE_URL, params=params)
        # response.raise_for_status() 
        data = response.json()
        
        if data.get('Response') == 'True':
            
            series_details = {
                'Title': data.get('Title', 'N/A'),
                'Season': sNumber,
                'Episode Number': epNumber,
                'Year': data.get('Year', 'N/A'),
                'Director': data.get('Director', 'N/A'),
                'IMDb Rating': data.get('imdbRating', 0),
                'Plot': data.get('Plot', 'N/A') 
            }
            print(series_details)
            return series_details
        else:
           
            return {"Error": data.get('Error', 'Movie not found.')}
            
    except requests.exceptions.RequestException as e:
        return {"Error": f"An error occurred while connecting to OMDb: {e}"}


# movieName = input('Enter Movie Name: ')
# get_movie_details(movieName)

# get_series_details()


# test to fetch random movies using char
# def get_movies():
    n = 10 
    seenID = set()
    movies = []

    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

    while len(movies) < n:
        x = random.choice(chars)
        param = {
            'type': 'movie', 
            'apikey': OMDB_API_KEY,
            's': x,
            'plot': 'short',
            'page': 1
        }
        response = request.args.get(OMDB_BASE_URL, params=param)
        data = response.json()
        print(f'fuck yeah: {x}')
        if "Search" in data:
            for i in data["Search"]:
                if i['imdbID'] not in seenID:
                    seenID.add(i['imdbID'])
                    movies.append(i)
                    print(f'fuck yeah: {len(movies)}')
                    if len(movies) > n:
                        break
        else:
            print("no bitch")
    return movies

# gotMovies = get_movies()
# print(f'lenght: {len(gotMovies)}')  


# def test1():    
    movies = []
     
    top_50_imdb_movies = ["The Shawshank Redemption","The Godfather","The Dark Knight","The Godfather Part II","12 Angry Men","The Lord of the Rings: The Return of the King","Schindler's List","The Lord of the Rings: The Fellowship of the Ring","Pulp Fiction","The Good, the Bad and the Ugly","Forrest Gump","Fight Club","The Lord of the Rings: The Two Towers","Inception","Spider-Man: Across the Spider-Verse","Star Wars: Episode V - The Empire Strikes Back","The Matrix","Goodfellas","One Flew Over the Cuckoo's Nest","Se7en","It's a Wonderful Life","Seven Samurai","Oppenheimer","The Silence of the Lambs","Interstellar","Saving Private Ryan","City of God","Life Is Beautiful","The Green Mile","Star Wars: Episode IV - A New Hope","Terminator 2: Judgment Day","Back to the Future","Spirited Away","The Pianist","Psycho","Parasite","Gladiator","The Lion King","Léon: The Professional","American History X","The Departed","Whiplash","The Prestige","The Usual Suspects","Casablanca","Grave of the Fireflies","Harakiri","The Intouchables","Modern Times","Cinema Paradiso"]
    for i in top_50_imdb_movies:
        params = {
        't': i,
        'apikey': OMDB_API_KEY,
        'plot': 'short'
        }        
        response = request.args.get(OMDB_BASE_URL, params=params)
        # response.raise_for_status() 
        data = response.json()
        
        if data.get('Response') == 'True':
            print("fuck ueah")
            movie_details = {
                'Title': data.get('Title', 'N/A'),
                'Year': data.get('Year', 'N/A'),
                'Director': data.get('Director', 'N/A'),
                'IMDb Rating': data.get('imdbRating', 0),
                'Plot': data.get('Plot', 'N/A') 
            }
            
            movies.append(movie_details)
 
    return movies

# mkbMovies = test1()
# print(f"ye le bsdk * {len(mkbMovies)}")

@app.route('/api/movies/genre', methods=['GET'])
def fetch_genre():

    genre = request.args.get('genre')
    genreList = genre.split(',')
    common_movie_words = ["Night", "Man", "Love", "Life", "Home", "Last", "Day", "Night", "World", "Girl", "Marvel", "Avengers"]
    movies = []
    found = False
    for s in common_movie_words:
        try:
            params = {
            's': s,
            'apikey': OMDB_API_KEY,
            'plot': 'short' 
            }

            response = requests.get(OMDB_BASE_URL, params=params)   
            response.raise_for_status() 
            search = response.json()
            print(search)
            for k in search["Search"]:
                i = k['imdbID']
                params1 = {
                'i': i,
                'apikey': OMDB_API_KEY,
                }
                response = requests.get(OMDB_BASE_URL, params=params1)
                #response.raise_for_status() 
                data = response.json()
                print(len(movies))
                for g in genreList:
                    if g in data['Genre']:
                        movie_details = {
                            'Title': data.get('Title', 'N/A'),
                            'imdbID': data.get('imdbID'),
                            'Year': data.get('Year', 'N/A'),
                            'Genre': data.get('Genre', 'N/A'),
                            'Director': data.get('Director', 'N/A'),
                            'imdbRating': data.get('imdbRating', 0),
                            'Plot': data.get('Plot', 'N/A'),
                            'Poster': data.get('Poster', 'N/A') 
                                }
                        movies.append(movie_details)                
                        if len(movies) > 4:
                            found = True
                            break
                    if found:
                        break
                if found:
                        break
        
  
        except requests.exceptions.RequestException as e:
            return {"Error": f"An error occurred while connecting to OMDb: {e}"}
        
        if found:
            break
        
    return movies

if __name__ == '__main__':
    app.run(debug=True)

# mkbMovies = fetch_genre()
# print(f'tmkc * {len(mkbMovies)}')

