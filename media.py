class Movie:
    """
    Movie Class
    """
    def __init__(self, movie_title, movie_poster_image_url, movie_trailer_youtube_url):
        """It called when object is created

        Args:
            movie_title(str): Title of movie
            movie_poster_image_url(str): Url of the poster
            movie_trailer_youtube_url(str): Url of the movie trailer
        """
        self.title = movie_title
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
