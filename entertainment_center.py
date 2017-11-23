# Import the necessary modules
import media
import fresh_tomatoes
# Create movie trailer objects by giving details
the_zeitgeist_movement = media.Movie("The Zeitgeist Movement",
                                     "TZM is a non-profit organization established inthe US 2008 by "
                                     "Peter Joseph in which it advocates a transformation of society and "
                                     "its economic system to a non-monetary system based on resource "
                                     "allocation and environmentalism.",
                                     "http://www.zeitgeistmovie.com/Zeitgeist%20moving%20forward.png.png",
                                     "https://www.youtube.com/watch?v=lx3JCdyB-q8")


the_choice_is_ours = media.Movie("The Choice is Ours",
                                 "The series shows an optimistic vision of the world if we apply science"
                                 " and technology for the benefit of all people and the environment.",
                                 "http://cdn.documentarylovers.com/wp-content/uploads/2015/03/the-choice-is-ours.jpg",
                                 "https://www.youtube.com/watch?v=RWEeNu2GC_o")

kymatica = media.Movie("Kymatica",
                       "A movie about universal consciousness.",
                       "https://i.ytimg.com/vi/eouOXlTvcGA/hqdefault.jpg",
                       "https://www.youtube.com/watch?v=yXwxS1_sSuM")

athene_theory_of_everything = media.Movie("Athene's Theory of Everything",
                                          "Athene's Theory of Everything is a 50 minute video with the main point "
                                          "being self-aware. Included is an outline with time links for those that "
                                          "prefer to digest in sections.",
                                          "http://smartlab.herts.ac.uk/wp-content/uploads/2014/04/biology_"
                                          "microscopic_cells_neurons_background_1920x1080_70373-600x400.jpg",
                                          "https://www.youtube.com/watch?v=HmEFQ3G89M4")



''' Some test for program'''
# print the_zeitgeist_movement.storyline
# print the_choice_is_ours.poster_image_url
# kymatica.show_trailer()
# print media.Movie.__doc__
# print media.Movie.VALID_RATINGS

# Create the list for storing movie trailer objects
movies = [the_zeitgeist_movement, the_choice_is_ours, kymatica, athene_theory_of_everything]

# Generate the movie trailer html page by calling open_movies_page function
fresh_tomatoes.open_movies_page(movies)



