import requests
import random
from bs4 import BeautifulSoup

URL = "http://www.imdb.com/chart/top"


def main():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    movietags = soup.select("td.titleColumn")
    inner_movietags = soup.select("td.titleColumn a")
    ratingtags = soup.select("td.posterColumn span[name=ir]")

    def get_year(movie_tag):
        movie_split = movie_tag.text.split()
        year = movie_split[-1] # last item
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list = [tag.get('title') for tag in inner_movietags]
    titles =  [tag.text for tag in inner_movietags]
    ratings = [float(tag.get('data-value')) for tag in ratingtags]

    n_movies = len(titles)
    while 1:
        idx = random.randrange(0, n_movies)

        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, starring: {actors_list[idx]}')

        user_input= input("Do you want another movie [y/[n]? ")
        if user_input.lower() != 'y':
            break


if __name__== "__main__":
    main()