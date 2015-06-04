import media
import fresh_tomatoes

# create a list variable to store the movie objects
movie_list = []

# create a movie object
wizard_of_oz =  media.Movie("The Wizard of Oz",
				"http://ia.media-imdb.com/images/M/MV5BMTU0MTA2OTIwNF5BMl5BanBnXkFtZTcwMzA0Njk3OA@@._V1_SY317_CR10,0,214,317_AL_.jpg",
				"https://www.youtube.com/watch?v=H_3T4DGw10U")
# add movie to list
movie_list.append(wizard_of_oz)

# create a movie object
titanic = media.Movie("Titanic",
                      "http://ia.media-imdb.com/images/M/MV5BMjExNzM0NDM0N15BMl5BanBnXkFtZTcwMzkxOTUwNw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
# add movie to list
movie_list.append(titanic)   

# create a movie object
matrix = media.Movie("The Matrix",
                     "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")
# add movie to list
movie_list.append(matrix)

# create a movie object
frozen = media.Movie("Frozen",
                     "http://resizing.flixster.com/M3JgYWjuLaOPruIuhLfHA0GwmtY=/180x267/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/35/11173584_ori.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
# add movie to list
movie_list.append(frozen)

# create a movie object
imitation_game = media.Movie("The Imitation Game",
                             "http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                             "https://www.youtube.com/watch?v=S5CjKEFb-sM")
# add movie to list
movie_list.append(imitation_game)

# create a movie object
star_wars = media.Movie("Star Wars: Episode VII - The Force Awakens",
                        "http://resizing.flixster.com/HBIJnzHib7pKy_C1Yxau8jyYhOg=/180x267/dkpu1ddg7pbsk.cloudfront.net/movie/11/18/17/11181757_ori.jpg",
                        "https://www.youtube.com/watch?v=OMOVFvcNfvE")
# add movie to list
movie_list.append(star_wars)

# call functions from fresh_tomotoes.py to create the content for all movies in list
fresh_tomatoes.create_movie_tiles_content(movie_list)

# use function from fresh_tomatoes.py to generate the HTML page to display the movie list
fresh_tomatoes.open_movies_page(movie_list)
