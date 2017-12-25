import webbrowser
class Movie():
    #the paths for youtube videos, and images on tmdb website.
    TMDB_IMAGE_PATH = 'https://image.tmdb.org/t/p/w640'
    YOUTUBE_VIDEO_PATH = 'https://www.youtube.com/watch?v='

    #construct the movie with the needed data.
    def __init__(self, movie_details, movie_videos):
        self.title = movie_details['title']
        
        self.storyline = movie_details['overview']
        
        self.poster_image_url = self.TMDB_IMAGE_PATH + movie_details['poster_path']
   
        self.trailer_youtube_url = self.YOUTUBE_VIDEO_PATH + movie_videos['results'][0]['key']

    #open a webpage with the data taken from the api.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


    

    
        
