import requests # type: ignore 
from flask import Flask,  request, render_template # type: ignore 

GenreURL = 'http://127.0.0.1:5000/api/movies/genre'
TitleSearchURL = 'http://127.0.0.1:5000/api/movie/title'

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recommendation')
def title_search():
    title=request.args.get('title')

    params = {'title': title}
    response = requests.get(TitleSearchURL, params=params)
    data0 = response.json()
    genre = data0['Genre']
  
    params = {'genre': genre}
    responseG = requests.get(GenreURL, params = params)
    data = responseG.json()
    sorted_movies = sorted(data, key=lambda x: float(x['imdbRating']), reverse=True)
    return render_template('recommendation.html', movies=sorted_movies)

    return data
    # return render_template(
    #                "recommendation.html",
    #                Title= sorted_rec_0.get('Title', 'N/A'),
    #                Genre= sorted_rec_0.get('Genre', 'N/A'),
    #                Director= sorted_rec_0.get('Director', 'N/A'),
    #                imdbRating= str(sorted_rec_0.get('imdbRating', 0)),
    #                Plot= sorted_rec_0.get('Plot', 'N/A'),
    #             #    Poster= sorted_rec_0.get('Poster', 'N/A')
    #                 )






if __name__ == '__main__':
    app.run(debug=True, port=5500)
