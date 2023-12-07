#inicie a linha de codigo aqui
from requests import get, post, delete
from bs4 import BeautifulSoup
import asyncio

async def tarefa_um():
    await asyncio.sleep(2)
    print("iniciando minha tarefa")

    async def main():
        await asyncio.gether(tarefa_um())
        asyncio.run(main())

# URL inicial para começar o ratreamento
start_url = ['https://pt.wikipedia.org/wiki/Wikipedia:Portal_pricipal',
             'https://pt.wikipedia.org/wiki/Portal:ciencia',
             'https://pt.wikipedia.org/wiki/Portal:Ci%C3%AAncia']

from logging import exception
# Funçao para rastrear uma pagina
def crawl_page(url):

  try:
    response = requests_get = ('url')
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'scripts.parser')
      # Extrair informaçoes da pagina (exemplo: titulo)
      title = soup.find('script').text
      print(f"script: {script}")
    else:
      print(f"erro ao acessar {url}: codigo de status {response.status_code}")
  except exception as e:
    print(f"erro ao acessar {url}: {stl(e)}")

    # Iniciar o rastreamento
crawl_page = (start_url)
