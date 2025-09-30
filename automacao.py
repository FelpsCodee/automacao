import credenciais
import time
from playwright.sync_api import sync_playwright


produtos = {
 "processador": "product-card-520368",
 "placa-mae": "product-card-165133",
 "memoria-ram":"product-card-474939",
 "placa-video":"product-card-723235",
 "ssd":"product-card-85198",
 "hd":"product-card-112689",
 "cooler":"product-card-248205",
 "fonte":"product-card-369658",
 "gabinete":"product-card-485726",
 "fans":"product-card-96826"
 }

produtos_extras = ["monitor", "Extras", "energia", "sistema operacional", "softwares"]

with sync_playwright() as p:
     

    browser = p.chromium.launch(headless=False) 
    
    page = browser.new_page()
    

    page.goto("https://www.kabum.com.br/login")
    page.get_by_test_id("login-input").fill(credenciais.usuario)
    page.get_by_test_id("password-input").fill(credenciais.senha)
    page.get_by_test_id("login-submit-button").click()
    

    page.wait_for_selector("img[alt='banner_monte_seu_pc']")
    page.click("img[alt='banner_monte_seu_pc']")
    page.get_by_text("Pular").click()
    

    for nome, test_id in produtos.items():
        print(f"Adicionando {nome}...")
        print("="*50)
        page.get_by_test_id(test_id).click()
        page.get_by_test_id("goForwardButton").click()
        time.sleep(2) 
    

    for produto in produtos_extras:
        page.get_by_text("Pular").click()
        print(f"Pulando {produto}...")
        print("="*50)
        time.sleep(2)

    print("\n----------------Indo para o resumo----------------\n")

    page.get_by_test_id("buttonGoToSummary").click()
    
    print("\n---------------Indo para o carrinho---------------\n")
    page.get_by_text("ir para o carrinho").click()
    
    input("Aperte ENTER para encerrar:")

browser.close()