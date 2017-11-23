# Movie Trailer Website

Write a movie trailer website in python and html programming.

## Getting Started

1. Install python 2.7 on your system;
2. Grab one of your favourite programming IDE or editor such as pycharm,vim;
3. The project consist of 3 major python source files

    |__ media.py  - Data structure for movie trailer website such as title,url,storyline,etc.

    |__ entertainment_center.py - Details of movie trailer data with each individual movie
      trailer as well as to call the open_movies_page(movies) from fresh_tomatoes module in
      order to generate the html page of movie trailer website

    |__ fresh_tomatoes.py - File offered by Udacity, the main idea of this python file is as following:

        1).open_movies_page(movies) function takes movies as its input;

        2).open and create a new html file with write mode;

        3).main_page_head expresses the structure of web page, the behaviour of trailer poster image
        when loading the page as well as how to play the trailer;

        4).the rendered_content is the keExplain how to run the automated tests for this systemy factor
        in this module where it extracts each trailer information includes id, title, url from the input
        list "movies" and put them all together using python foramt() function insert those information
        into the html code in which the code describes how each trailer expresses in the page;

        5).create an url object to store the absolute path of the generated html file then call the
        default web browser to open the page.

## Running of the test

After you run the entertainment_center.py file then the html file is generated in the same folder,
the web page will be opened in the browser by default, check the movie trailers and click each of
those poster_image, the trailer video will autoplay respectively in the form of embedded video.

## Get the source code

You can download, check and run the python program by the link down below.

[github link for movie trailer website](https://github.com/loveplay1983/python_movie_trailer_website)

## Acknowledgments

* Udacity online courses all teachers
* Python course teachers
* classmates, friends, python developers within the community, etc.
