import webbrowser

class Movie():

        # creates the movie object and sets the values for instance variables
	def __init__(self,title,poster_image,trailer):
		self.title = title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer

        # displays the trailer video
	def show_trailer(self):
		webbrowser.open(self.trailer)
