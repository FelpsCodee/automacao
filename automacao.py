import credenciais
import time
from playwright.sync_api import Playwright, sync_playwright, expect

 #LISTAS DOS PRODUTOS PARA O FLUXO
produtos = {
 "processador": "product-card-520368",
 "placa-mae": "product-card-165133",
 "memoria-ram":"product-card-474939",
 "placa-video":"product-card-723235",
 "hd":"product-card-112689",
 "cooler":"product-card-248205",
 "fonte":"product-card-369658",
 "gabinete":"product-card-324516",
 "fans":"product-card-96826",
 }

with sync_playwright() as p:
     
 #TIPO DE NAVEGADOR
    navegador = p.chromium.launch(headless=False) 
    #GERAR UMA PAGINA
    pagina = navegador.new_page()
    
    #LOGIN
    pagina.goto("https://www.kabum.com.br/login")
    pagina.get_by_test_id("login-input").fill(credenciais.usuario)
    pagina.get_by_test_id("password-input").fill(credenciais.senha)
    pagina.get_by_test_id("login-submit-button").click()
    
    #IR PARA O MONTE O SEU PELO BANNER SUPEIOR DIREITO
    pagina.wait_for_selector("img[alt='banner_monte_seu_pc']")
    pagina.click("img[alt='banner_monte_seu_pc']")
    pagina.get_by_text("Pular").click()
    
    #LOGICA PARA ESCOLHER PEÇAS NO MONTE O SEU
    for nome, test_id in produtos.items():
        print(f"Adicionando {nome}...")
        print("="*50)
        pagina.get_by_test_id(test_id).click()
        pagina.get_by_test_id("goForwardButton").click()
        time.sleep(2) 

    #FECHAMENTO DO NAVEGADOR
navegador.close()