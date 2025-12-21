import requests # Biblioteca de requisições http

# criando função para pesquisar produtos na api

def pesquisar_produtos(api_url, max_pages=100):

    pagina_atual = 1
    while pagina_atual != max_pages:

        response = requests.get(f"{api_url}?page={pagina_atual}")
        dados = response.json()
        for produto in dados['products']:
            yield produto
        if 'next_page' not in dados:
            break
        pagina_atual += 1

for produto in pesquisar_produtos("https://api.exemplo.com/products"):

    print(produto['name'])