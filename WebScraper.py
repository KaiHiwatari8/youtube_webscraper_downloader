import requests
from bs4 import BeautifulSoup as bs


class scraper():
    def __init__(self, url_path):
        self.url_path = url_path
        self.details = {}

    def scrap(self):
        self.response = requests.get(self.url_path)
        self.soup = bs(self.response.content, 'html5lib')
        self.details['Video title'] = self.soup.find_all('span', attrs={'class':'watch-title'})[0].text.strip()
        self.details['Video Description'] = self.soup.find_all('div',attrs={'id':'watch-description-text'})[0].text.strip()
        self.details['View cnt'] =  self.soup.find_all('div', attrs={'class':'watch-view-count'})[0].text.strip()
        self.details['Likes'] = self.soup.find_all('button',attrs={'title':'I like this'})[0].text.strip()
        self.details['Dislikes'] = self.soup.find_all('button',attrs={'title':'I dislike this'})[0].text.strip()
        self.details['Category'] = self.soup.find_all('ul', attrs={'class':'content watch-info-tag-list'})[0].text.strip()

    def get_details(self):
        return dict(self.details)

    def __str__(self):
        answer = 'Video URL: ' + self.url_path + '\n'
        for key,value in self.details.items():
            answer += key + ': ' + value + '\n\n'
        return answer
