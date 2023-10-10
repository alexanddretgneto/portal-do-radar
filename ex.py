import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url_base = 'https://lista.mercadolivre.com.br/'
produto_nome = input('Qual produto você deseja? ')
print() 

# Concatene a consulta de pesquisa à URL
url = url_base + produto_nome

response = requests.get(url, headers=headers)

site = BeautifulSoup(response.text, 'html.parser')

# Encontre todos os resultados de produtos
produtos = site.find_all('div', class_='andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16')

# Crie uma lista para armazenar os produtos com títulos, preços e URLs de imagem
lista_produtos = []

# Percorra os resultados e adicione os títulos, preços e URLs de imagem à lista
for produto in produtos:
    titulo = produto.find('h2', class_='ui-search-item__title')
    preco_element = produto.find('span', class_='andes-money-amount__fraction')
    imagem_element = produto.find('img', class_='ui-search-result-image__element')
    
    if titulo and preco_element and imagem_element:
        titulo_text = titulo.text.strip()
        preco_text = preco_element.text.strip()
        
        # Converta o preço de texto para um número (removendo vírgulas e pontos)
        preco_numero = float(preco_text.replace(',', '').replace('.', ''))
        
        # Obtenha a URL da imagem
        imagem_url = imagem_element.get('src')
        
        # Adicione o produto à lista de produtos
        lista_produtos.append((titulo_text, preco_numero, imagem_url))

# Ordene a lista de produtos com base no preço (do menor para o maior)
lista_produtos_ordenada = sorted(lista_produtos, key=lambda x: x[1])

# Percorra a lista ordenada e imprima os produtos com suas URLs de imagem
for produto in lista_produtos_ordenada:
    titulo_text, preco_numero, imagem_url = produto
    print(f"Produto: {titulo_text}")
    print(f"Preço: R${preco_numero:,.2f}")
    print(f"Imagem URL: {imagem_url}")
    print()

