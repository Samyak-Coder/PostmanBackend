# data = {"Search":[{"Title":"Night at the Museum","Year":"2006","imdbID":"tt0477347","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BNGMyYjYyZDAtNzRiZC00ZjRkLTkwYjktODkxODQzNTFiMTVmXkEyXkFqcGc@._V1_SX300.jpg"},{"Title":"Game Night","Year":"2018","imdbID":"tt2704998","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BMjI3ODkzNDk5MF5BMl5BanBnXkFtZTgwNTEyNjY2NDM@._V1_SX300.jpg"},{"Title":"Night at the Museum: Battle of the Smithsonian","Year":"2009","imdbID":"tt1078912","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BY2E0NTRjMDEtMWI3NS00YTRmLTg4NmEtNzIxZjQ3YWM2NDQxXkEyXkFqcGc@._V1_SX300.jpg"},{"Title":"30 Days of Night","Year":"2007","imdbID":"tt0389722","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BZWVjOTM3NmItZjU1Mi00YTVjLTlkM2YtNTJlYjI2YzUyNmUxXkEyXkFqcGc@._V1_SX300.jpg"},{"Title":"Last Night in Soho","Year":"2021","imdbID":"tt9639470","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BODdhZjBmZTEtZmQyMy00NWY5LWJiMWQtODhjODFkZWZlMjMyXkEyXkFqcGc@._V1_SX300.jpg"},{"Title":"Date Night","Year":"2010","imdbID":"tt1279935","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BYjVjMzIyZTgtMjQwZS00ODA1LTllY2YtZDhkNjA1OTQ3NjliXkEyXkFqcGc@._V1_SX300.jpg"},{"Title":"Night of the Living Dead","Year":"1968","imdbID":"tt0063350","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BZGMyZTA0MWEtZjczMS00ZDE5LTk1OTQtNmIxNGYzNDA2NDVhXkEyXkFqcGc@._V1_SX300.jpg"},{"Title":"Night at the Museum: Secret of the Tomb","Year":"2014","imdbID":"tt2692250","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BMjI1MzM2ODEyMV5BMl5BanBnXkFtZTgwNTIzODAwMzE@._V1_SX300.jpg"},{"Title":"Late Night with the Devil","Year":"2023","imdbID":"tt14966898","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BYTRiNWZlNGMtOTUwZi00ZjE4LWE1ZjEtNWE4MGQ2ZGU5NDliXkEyXkFqcGc@._V1_SX300.jpg"},{"Title":"Run All Night","Year":"2015","imdbID":"tt2199571","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BMTU2ODI3ODEyOV5BMl5BanBnXkFtZTgwMTM3NTQzNDE@._V1_SX300.jpg"}],"totalResults":"10579","Response":"True"}

# data = {"Title":"The Avengers","Year":"2012","Rated":"PG-13","Released":"04 May 2012","Runtime":"143 min","Genre":"Action, Sci-Fi","Director":"Joss Whedon","Writer":"Joss Whedon, Zak Penn","Actors":"Robert Downey Jr., Chris Evans, Scarlett Johansson","Plot":"Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.","Language":"English, Russian","Country":"United States","Awards":"Nominated for 1 Oscar. 39 wins & 81 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BNGE0YTVjNzUtNzJjOS00NGNlLTgxMzctZTY4YTE1Y2Y1ZTU4XkEyXkFqcGc@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.0/10"},{"Source":"Rotten Tomatoes","Value":"91%"},{"Source":"Metacritic","Value":"69/100"}],"Metascore":"69","imdbRating":"8.0","imdbVotes":"1,528,141","imdbID":"tt0848228","Type":"movie","DVD":"N/A","BoxOffice":"$623,357,910","Production":"N/A","Website":"N/A","Response":"True"}
# for i in data["Search"]:
#     k = i['imdbID'] 
#     print(k)

# if 'Action' in data["Genre"]:
#     print('fuck yes')

# import requests # type: ignore 
# from flask import Flask, render_template, request, redirect, url_for # type: ignore 
# import random


# OMDB_API_KEY = "1394625b"
# OMDB_BASE_URL = "http://www.omdbapi.com/"

# movies = []

# params = {
#     's': '',
#     'apikey': OMDB_API_KEY,
#     'plot': 'short'
# }

# response = requests.get(OMDB_BASE_URL, params=params)
# # response.raise_for_status() 
# search = response.json()
# print(search)
# for i in search["Search"]:
#     params1 = {
#     'i': i,
#     'apikey': OMDB_API_KEY,
#     'plot': 'short'
#     }
#     response = requests.get(OMDB_BASE_URL, params=params1)
#     # response.raise_for_status() 
#     data = response.json()
#     if 'Action' in data['Genre']:
#         movies.append(data)                
#         if len(movies) == 15:
            # break


# genre = 'Action, Scifo'
# test = genre.split()

# testData = "Action, Romantic, comedy, Scifo"

# for i in test:
#     if i in testData:
#         print('tmkc')
#     else:
#         print('phuk')

# imdbID = data['imdbID']


# employees = {
#     'john': {'age': 30, 'salary': 50000, 'id': 1},
#     'jane': {'age': 25, 'salary': 60000, 'id': 2},
#     'peter': {'age': 35, 'salary': 55000,'id': 3 }
# }

# sortE = dict(sorted(employees.items(), key=lambda item: item[1]['age']))
# print()



import requests # type: ignore 
from flask import Flask, render_template, request   # type: ignore 
import random
import os
from dotenv import load_dotenv

load_dotenv() 
app = Flask(__name__)

OMDB_API_KEY = os.getenv("API_KEY")
OMDB_BASE_URL = "http://www.omdbapi.com/"  

      
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recommendation')
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
                'imdbRating': float(data.get('imdbRating', '0')),
                'Plot': data.get('Plot', 'N/A'),
                'Poster': data.get('Poster', 'N/A') 
            }
            return render_template(
                   "recommendation.html",
                   Title= movie_details.get('Title', 'N/A'),
                   Year= movie_details.get('Year', 'N/A'),
                   Genre= movie_details.get('Genre', 'N/A'),
                   Director= movie_details.get('Director', 'N/A'),
                #    imdbRating= movie_details.get('imdbRating', 0),
                   Plot= movie_details.get('Plot', 'N/A'),
                   Poster= movie_details.get('Poster', 'N/A')
            )
        
        else:
           
            return {"Error": data.get('Error', 'Movie not found.')}
            
    except requests.exceptions.RequestException as e:
        return {"Error": f"An error occurred while connecting to OMDb: {e}"}
    
if __name__ == '__main__':
    app.run(debug=True, port=5500)
