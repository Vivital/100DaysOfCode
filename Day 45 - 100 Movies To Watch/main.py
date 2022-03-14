import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movies = [film.text for film in soup.find_all(name="h3", class_="title")]
movies = movies[::-1]

with open("movies.txt", "w", encoding="utf-8") as data:
    for i in movies:
        data.write(f"{i}\n")
