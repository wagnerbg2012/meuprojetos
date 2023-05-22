#Instalação da lib do Selenium
#pip3 install selenium

#Instalção beutifulsoupo
#pip3 install beautifulsoup4

#instalação do lxml
#pip3 install lxml

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup #Responsavel pela extração de dados
from time import sleep

import pandas as pd

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

# Passo 1: Acessar pagina
link = "http://sac.ikhon.com.br/sac"
navegador.get(url=link)


# Passo 2: longar na pagina
navegador.find_element('xpath', '//*[@id="txt_login"]').send_keys("wagner.gama@ikhon.com.br")
navegador.find_element('xpath', '//*[@id="txt_senha"]').send_keys("Nescafe@1504")
navegador.find_element('xpath', '//*[@id="acao"]').click()


# Passo 3: acessar projeto
#link do projeto SGD-ATI
link = "http://sac.ikhon.com.br/sac/Controle?bl=Listagem&am=&idProjeto[]=248"  
site = navegador.get(link)

#Seleciona SAC
navegador.find_element('xpath', '//*[@id="tblExport"]/table/tbody/tr[3]/td[2]/a').click()

