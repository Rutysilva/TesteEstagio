import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.tjpb.jus.br/comarcas/lista'

driver.get(url)

checkbox = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
checkbox.click()

titleElements = driver.find_elements(By.CLASS_NAME, 'link-modal-comarca')

nomes_cidades = [title.text for title in titleElements if title.text.strip() != '']


juizes = []

for i in range (len (titleElements)) :
    
    titleElements[i].click()

    WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
    
    trs = driver.find_elements(By.TAG_NAME, 'tr')
    textos_trs = []

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, 'td') 
        textos_tds = [td.text for td in tds if td.text.strip()] 
        if textos_tds:
            textos_trs.append(textos_tds)
    
    juizes.append(textos_trs)
    close_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'close'))
    )
    close_button.click()
    time.sleep(1)

comarcas_juizes = []
for cidade, juris in zip(nomes_cidades, juizes):
    comarcas_juizes.append({'Cidade': cidade, 'Juízes': juris})

for comarca in comarcas_juizes:
    print(f"Cidade: {comarca['Cidade']}")
    for juiz in comarca['Juízes']:
        print(f"  - Jurisdição: {juiz[0]} | Juiz: {juiz[1]}")
    print()

dictComarca = {'Cidade': nomes_cidades, 'Jurisdições': juizes}

df = pd.DataFrame
