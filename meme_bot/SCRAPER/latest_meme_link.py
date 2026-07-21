import requests
from bs4 import BeautifulSoup
from .headers import headers

def get_latest_meme_link():
    
    url = "https://knowyourmeme.com/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    latest = soup.select_one(".fresh-entries .wide-card:first-of-type")
    if not latest:
        return None
    
    link = "https://knowyourmeme.com" + latest["href"]

    return link


