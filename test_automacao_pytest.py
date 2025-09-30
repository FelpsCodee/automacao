import pytest
import requests

def test_api_retorna_200():
   url = "https://www.kabum.com.br"
   
   headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

   response  = requests.get(url, headers=headers)
   assert response.status_code == 200

def test_verificar_mouses():
      url_api = "https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/products-by-category/perifericos/-mouse-gamer?page_number=1&page_size=100&facet_filters=&sort=most_searched&is_prime=true&payload_data=products_category_filters&include=gift"
      termo = "Mouse"      
      
      parametros = {
            'query': termo,
            'page_size':100,
            'sort': 'most_searched',
            'is_prime':'true',
      }
      
      nome_produtos = []
      response = requests.get(url_api, params=parametros)
      dados = response.json()

      
      assert len(dados['data']) > 0
      
      listas_de_produtos = dados['data']
      
      for produto in listas_de_produtos:
        mouses = produto['attributes']['title']
        nome_produtos.append(mouses)
        
        
        print(nome_produtos)
       
      print(f"foram {len(nome_produtos)} produtos encontrados")
      
      for produto in nome_produtos:
            assert termo in produto

test_verificar_mouses()

