import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20190627165544/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
data = response.text

# Write your code below this line 👇
soup = BeautifulSoup(data, "html.parser")
list = [name.text for name in soup.select("h2")]
list.reverse()

file_path = r"Projects\Web Scraping\Starting Code - 100 movies to watch start\movies.txt"
with open(file_path, mode='w', encoding='utf-8') as file:
    for movie in list:
        file.write(movie + '\n')
