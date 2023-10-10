# pesquisa/views.py
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def pesquisar_produto(request):
    if request.method == 'POST':
        produto_nome = request.POST['produto_nome']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        url_base = 'https://lista.mercadolivre.com.br/'
        url = url_base + produto_nome

        response = requests.get(url, headers=headers)
        site = BeautifulSoup(response.text, 'html.parser')

        produtos = site.find_all('div', class_='andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16')

        lista_produtos = []

        for produto in produtos:
            titulo = produto.find('h2', class_='ui-search-item__title')
            preco_element = produto.find('span', class_='andes-money-amount__fraction')
            imagem_element = produto.find('img', class_='ui-search-result-image__element')

            if titulo and preco_element and imagem_element:
                titulo_text = titulo.text.strip()
                preco_text = preco_element.text.strip()
                preco_numero = float(preco_text.replace(',', '').replace('.', ''))
                imagem_url = imagem_element.get('src')

                lista_produtos.append((titulo_text, preco_numero, imagem_url))

        lista_produtos_ordenada = sorted(lista_produtos, key=lambda x: x[1])

        return render(request, 'pesquisa/resultado.html', {'produtos': lista_produtos_ordenada})

    return render(request, 'pesquisa/pesquisa.html')
