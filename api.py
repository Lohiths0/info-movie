import requests, json

movie = input("Movie: ")
url = "http://www.omdbapi.com/?apikey=319ff967&t="+movie
movieJson = requests.get(url)
movieInfo = movieJson.json()
imdbRating =  movieInfo['Ratings'][0]['Value']
rottenTomRating = movieInfo['Ratings'][1]['Value']
metacriticRating = movieInfo['Ratings'][2]['Value']
plot =  movieInfo['Plot']
imdbId = movieInfo['imdbID']

def movieRev (Id):
    url = "https://api.themoviedb.org/3/movie/"+Id+"/reviews?api_key=a99641208e392385752e7b64b4b6c3f7&language=en-US&page=1"
    print (url)
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    reviews = []
    reviews.append(response.json()['results'][0]['content'])
    reviews.append(response.json()['results'][1]['content'])
    reviews.append(response.json()['results'][2]['content'])
    print (reviews)



print (movieInfo)
print (imdbId)
movieRev(imdbId)

