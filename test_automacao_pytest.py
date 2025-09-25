import pytest
import requests

def test_api_retorna_200():
   url = "https://www.kabum.com.br"
   
   headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

   response  = requests.get(url, headers=headers)
   assert response.status_code == 200
   
import requests

def test_api_autocomplete_kabum_sugere_termo_correto():
      url_api = "https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/sponsored_products?query=rtx%205060&context=search"
      termo = "RTX 5060"
      
      response = requests.get(url_api)
      response_em_json = response.json()

      status = response.status_code
      print()
      print(status)

test_api_autocomplete_kabum_sugere_termo_correto()      
      
   