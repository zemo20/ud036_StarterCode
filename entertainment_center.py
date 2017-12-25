import media
import fresh_tomatoes
import tmdbsimple as tmdb
import urllib.request
import json

#API KEY of TMDB API
API_KEY='2a3e6da5f121dd9f07a5fb18fd1afc43'
#Base url of TMDB APIs
FIND_MOVIE_API='https://api.themoviedb.org/3/movie/'
#list of movie IDs to search for
movie_ids_list = [110,327,128,541,975,574]
movie_list = []

#find movie details throught the api
def _get_movie_details(movie_id):
     request_string = FIND_MOVIE_API + str(movie_id) +'?api_key='+API_KEY
     connection = urllib.request.urlopen(request_string)
     output = json.loads(connection.read().decode("utf-8"))
     return output

    
     
#find trailer which have a different api than the other details
def _get_movie_videos(movie_id):  
   request_string = FIND_MOVIE_API + str(movie_id) +'/videos?api_key='+API_KEY
   connection = urllib.request.urlopen(request_string)
   output = json.loads(connection.read().decode("utf-8"))
   return output

#append movie_list with movies we searched for
for x in range(0,6):
    movie_id = movie_ids_list[x]
    movie_list.append(media.Movie(_get_movie_details(movie_id),
                                  _get_movie_videos(movie_id)))


    


fresh_tomatoes.open_movies_page(movie_list)
