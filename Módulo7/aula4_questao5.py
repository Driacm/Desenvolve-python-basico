import csv

# Lista de livros com título, autor, ano de publicação e número de páginas
livros = [
    ["O Grande Sertão Veredas", "Joao Guimaraes Rosa", "1956", "600"],
    ["O triste fim de Policarpo Quaresma", "Machado de Assis", "1915", "300"],
    ["A Arte da Guerra", "Sun Tzu", "5 a.C.", "272"],
    ["O Sol é para Todos", "Harper Lee", "1960", "281"],
    ["O Morro dos Ventos Uivantes", "Emily Bronte", "1847", "400"],
    ["A Menina que Roubava Livros", "Markus Zusak", "2005", "552"],
    ["Metamorfose", "Frans Kafka", "1915", "100"],
    ["A cegueira branca", "Saramago", "2004", "400"],
    ["O menino do Engenho", "José Lins do Rego", "1932", "250"],
    ["A Esperança", "Suzanne Collins", "2010", "391"]
]

# Nome do arquivo CSV
nome_arquivo = 'meuslivros.csv'

# Abre o arquivo para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escreve o cabeçalho
    writer.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escreve as linhas com as informações dos livros
    writer.writerows(livros)

print(f'Arquivo "{nome_arquivo}" criado com sucesso!')