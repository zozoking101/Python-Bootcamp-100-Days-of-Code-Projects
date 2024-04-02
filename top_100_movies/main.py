# import requests
from bs4 import BeautifulSoup

URL = 'https://www.empireonline.com/movies/features/best-movies-2'

# response = requests.get(URL)
# print(response.status_code)
# data = response.text
#
# soup = BeautifulSoup(data, 'html.parser')
# pretty_soup = soup.prettify()
#
# with open("top_100_movies.txt", mode="w") as f:
#     f.write(pretty_soup)

with open("top_100_movies.txt", mode="r") as f:
    content = f.read()

movie_soup = BeautifulSoup(content, "html.parser")
top_100_movies = movie_soup.find_all(name="h3",
                                     class_="listicleItem_listicle-item__title__BfenH")
movie_names = [i.getText().replace("\n", "").strip().split(")")[1] \
               for i in top_100_movies]
# print(movie_names)

movie_names_1_to_100 = movie_names[::-1]
print(movie_names_1_to_100)

with open("movie_names.txt", mode="w") as f:
    for i in range(len(movie_names_1_to_100)):
        f.write(f"{i + 1}) {movie_names_1_to_100[i]}.\n")
