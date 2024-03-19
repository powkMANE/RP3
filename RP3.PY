from bs4 import BeautifulSoup
import requests
import re

def link_extractor(url):
    url = "https://trojka.polskieradio.pl/playlista"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    artists = soup.findall(class="PlaylistItem_songArtist__WzHEJ") 
    titles = soup.findall(class="PlaylistItem_songTitle__ZuWmJ")
