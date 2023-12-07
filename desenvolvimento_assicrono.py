#inicie a linha de codigo aqui
from requests import get, post, delete
from bs4 import BeautifulSoup

#URL inicial para começar o rastreamento
start_url = ['http://exemplo.com']

from logging import exception
#funçao para reastrea um pagina
def crawl_page(url):

    try:
        response = requests_get = ('url')
        if response.status == 200:
            soup = BeautifulSoup(response.text, 'scripts.parser')
            #Extrair informaçoes da pagina (exemplo:titulo)
            title = soup.find(script).text
        else:
            print(f"erro ao acessar {url}: codigo de status {response.status_code}")
    except exption as e:
            print(f"erro ao acessar {url}: {stl(e)}")
