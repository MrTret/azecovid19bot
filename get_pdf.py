import os

import requests
from bs4 import BeautifulSoup
from wand.image import Image


def pdf():
    url2 = "https://koronavirusinfo.az"
    return f"{url2}{BeautifulSoup(requests.get(url2).text, 'lxml').find_all('div', class_='fullheight_information container')[0].find('div', class_='buttons_div').find('a').get('href')}"


def download():
    with open('pdf.pdf', 'wb') as file:
        file.write(requests.get(pdf()).content)
        file.close()


def convert():
    with Image(filename="pdf.pdf", resolution=300) as img:
        img.format = 'jpg'
        img.compression_quality = 100
        img.save(filename='covid19.jpg')


def remove():
    os.remove("pdf.pdf")
    os.remove("covid19.jpg")
