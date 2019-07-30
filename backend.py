from flask import Flask, render_template, request, redirect
import requests, json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/namemovie/test', methods=['GET', 'POST'])

def moviePageDisplay():
    
    result = "invalid movie"
    if request.method == 'POST' or request.method == 'GET':
        result = request.form['nameMovie']
        aboutMovie = loadMovieData(result)
        #aboutMovieJSON = json.dumps(aboutMovie)
    
    revList = aboutMovie['movieReviewList'].strip('][').split('---------------') 
    ##return render_template('movie.html', imdbRate = aboutMovie['imdbRating'], metaRate = aboutMovie['metacriticRating'], rotRate = aboutMovie['rottenTomRating'], plot = aboutMovie['plot'], rev0 = aboutMovie['movieReviewList'][0], rev1 = aboutMovie['movieReviewList'][1], rev2 = aboutMovie['movieReviewList'][2] )
    return render_template('movie.html', imdbRate = aboutMovie['imdbRating'], metaRate = aboutMovie['metacriticRating'], rotRate = aboutMovie['rottenTomRating'], plot = aboutMovie['plot'], rev0 = revList[0], rev1 = revList[1], rev2 = revList[2], movieName = result, youtubeLink = aboutMovie['youtubeLink'] )
    
    


def loadMovieData(movie):
    url = "http://www.omdbapi.com/?apikey=319ff967&t="+movie
    movieJson = requests.get(url)   
    movieInfo = movieJson.json()
    imdbRating =  movieInfo['Ratings'][0]['Value']
    rottenTomRating = movieInfo['Ratings'][1]['Value']
    metacriticRating = movieInfo['Ratings'][2]['Value']
    plot =  movieInfo['Plot']
    imdbId = movieInfo['imdbID']
    movieReviewList = movieRev(imdbId)

    youtubeKey = trailerLink(imdbId)
    youtubeLink = "https://www.youtube.com/embed/"+youtubeKey+'?autoplay=1'

    allData = [imdbRating, rottenTomRating, metacriticRating, plot, imdbId, movieReviewList]
    allDataJson = {'imdbRating':imdbRating, 'rottenTomRating': rottenTomRating, 'metacriticRating':metacriticRating, 'plot': plot, 'imdbId':imdbId, 'movieReviewList':movieReviewList, 'youtubeLink': youtubeLink}
 
    
    return allDataJson


def movieRev (Id):
    url = "https://api.themoviedb.org/3/movie/"+Id+"/reviews?api_key=a99641208e392385752e7b64b4b6c3f7&language=en-US&page=1"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    reviews = []

    reviews.append(response.json()['results'][0]['content'])
    reviews.append("---------------")
    reviews.append(response.json()['results'][1]['content'])
    reviews.append("---------------")
    reviews.append(response.json()['results'][2]['content'])
    return str(reviews)

def trailerLink(Id):
    url = "https://api.themoviedb.org/3/movie/"+Id+"/videos?api_key=a99641208e392385752e7b64b4b6c3f7&language=en-US&page=1"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    youtubeKey = response.json()['results'][0]['key']
    return youtubeKey

if __name__ == '__main__':
   app.run(debug = True)