# Lista de URLs fornecida
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Criação da lista de domínios utilizando fatiamento
dominios = [url[4:-4].capitalize() for url in urls]

# Exibição da lista de domínios
print(dominios)