from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def noticias(request):
    url = "https://g1.globo.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('div', class_='feed-post-body')
        noticias_list = []

        for index, headline in enumerate(headlines, start=1):
            headline_text = headline.find('a', class_='feed-post-link').text
            news_link = headline.find('a', class_='feed-post-link').get('href')  # Obtém a URL da notícia
            image_element = headline.find('img', class_='bstn-fd-picture-image')
            image_url = image_element.get('src')  # Obtém a URL da imagem
            noticias_list.append({'title': headline_text, 'image_url': image_url, 'news_link': news_link})

        return render(request, 'noticias.html', {'noticias_list': noticias_list})
    else:
        return render(request, 'error.html', {'status_code': response.status_code})




