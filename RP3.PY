from bs4 import BeautifulSoup
import requests
import re
import xlsxwriter
from datetime import datetime

url = 'https://malopolskie-media.info/playlista/polskie-radio-trojka/2024-02-26/0/24.html'
songs_list = []
def link_extractor(url):
#    url = input("Provide the link to the OST: ")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    songs = soup.find_all('a')
    for element in songs:
        songs_list.append(element.get_text())
    
link_extractor(url)

only_songs = []

for song in songs_list:
    if '-' in song and '\n' not in song:
        only_songs.append(song)

dt = datetime.now()
ts = datetime.timestamp(dt)

WBName = 'Songs_' + str(ts) + '.xlsx'
workbook = xlsxwriter.Workbook(WBName)
worksheet = workbook.add_worksheet()
row = 0
col = 0

for song in only_songs:
    worksheet.write(row, col, song)
    row += 1
workbook.close()




