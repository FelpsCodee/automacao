import pytest
import requests
import pprint

def test_api_retorna_200():
   url = "https://www.kabum.com.br"
   
   headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

   response  = requests.get(url, headers=headers)
   assert response.status_code == 200
   
import requests

def test_api_autocomplete_kabum_sugere_termo_correto():
      url_api = "https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/search"
      termo = "mouse"      
      
      parametros = {
            'query': termo,
            'page_size':5,
            'sort': 'most_searched',
            'is_prime':'true',
      }
      
      
      response = requests.get(url_api, parametros)
      dados = response.json()
      print(dados['title'])
      
      assert len(dados['products']) > 0
      
      listas_de_produtos = dados['products']
      
      for produto in listas_de_produtos:
            nome_produtos = produto['name']
            
      
      assert  termo.lower in nome_produtos
      
test_api_autocomplete_kabum_sugere_termo_correto()

