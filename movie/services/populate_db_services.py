from bs4 import BeautifulSoup
import requests


class PopulateDBService():
    def __init__(self, data):
        self.data = data
        self.url = data['url']

    def extract_details(self):
        self.extract_soup()
        self.extract_movie_links()
        self.extract_movie_details( url = '/title/tt0111161/')

    def extract_soup(self):
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.text, 'html.parser')
        
    def extract_movie_links(self):
        self.movie_links = []
        for link in self.soup.find_all('a'):
            href = link.get('href')
            if href:
                if href.startswith('/title/') and href not in self.movie_links:
                    self.movie_links.append(link.get('href'))


    def extract_movie_details(self, url):
        r = requests.get( 'https://www.imdb.com'+ url)
        movie_soup = BeautifulSoup(r.text, 'html.parser')
        movie_title = movie_soup.title.string.split('- IMDb')[0]
        try:
            imdb_rating = movie_soup.find("span", itemprop="ratingValue").string
        except:
            imdb_rating = None
        try:
            summary_text = movie_soup.find("div", class_="summary_text").string
        except:
            summary_text = None

        return {
            'movie_title': movie_title,
            'imdb_rating': imdb_rating,
            'summary_text': summary_text
        }
    
    def save_movie_in_db(movie_data):
        pass