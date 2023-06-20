from turtle import towards
import requests 
import json
from bs4 import BeautifulSoup 


def encontraCategoria(noticia, valorPadrao=""):
    categoria = noticia
    if categoria is None:
        return valorPadrao
    else:
        return noticia.text

def encontraTitulo(noticia, valorPadrao=""):
    titulo = noticia
    if titulo is None:
        return valorPadrao
    else:
        return noticia.text


res = requests.get("https://canalsolar.com.br/noticias/")
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

noticias = soup.find_all(class_="inner")

todasNoticias = []

for noticia in noticias:
    categoriaLocalizacao = noticia.find(class_="meta-category")
    categoria = encontraCategoria(categoriaLocalizacao)
    tituloLocalizacao = noticia.find(class_="post-heading")
    titulo = encontraTitulo(tituloLocalizacao)

    todasNoticias.append({
        "categoria": categoria, 
        "titulo": titulo})

agrupaNoticia = {}

for noticia in todasNoticias:
    agrupaNoticia.setdefault(noticia["categoria"], []).append(noticia)

for noticia in agrupaNoticia:
    for post in noticia:
        post.pop(post["categoria"])

print(agrupaNoticia)

with open("noticias.json", "w") as json_file: 
    json.dump(agrupaNoticia, json_file, indent=3, ensure_ascii=False)