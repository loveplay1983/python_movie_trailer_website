# Import the webbrowser module for browser operation
import webbrowser
# This class defines the main data structure for movie trailer such as title,storyline,
# poster_image_url and trailer_youtube_url
class Movie():

    '''
    This class contains the basic data structure to store the favourite movie trailer information,
    including the movie title, poster_image_url and the youtube_movie_url,etc.
    '''

    # Movie Rating(HINT: constant value is often remain upper case)
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image_url,trailer_youtube_url):
        # This part is so called constructor in python programming
        # It used to be initializing the data structure
        self.title = movie_title
        self.storyline = movie_storyline
        # self keyword means the class object itself is being created,
        # it is somewhat similar to other OOP environment for example Java(this)
        # practice the condition with or without self keyword
        # storyline = movie_storyline_url
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        # Open the specific trailer_youtube_url in web browser,
        # This function only for testing
        webbrowser.open(self.trailer_youtube_url)
