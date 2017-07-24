#python 3.5.2 selenium 3.4
from selenium import webdriver
from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup
#from urllib.request import urlopen
import time
import sys

driver = webdriver.PhantomJS('./phantomjs') # navegador phantom js


url_siga = "https://siga.udesc.br/sigaSecurityG5/?pcaes=a205de9c60d3992e6296830743168a74"
url_notas = "https://siga.udesc.br/siga/com/executaconsultapersonaliz.do?evento=executaConsulta&id=2&exe=S"
driver.get(url_siga) #abre o pocilga

time.sleep(0.1) #ajax??
driver.find_element(By.XPATH,'//*[@id="senha"]').send_keys("senha") #manda a senha para o textfield
time.sleep(0.1) #ajax??
driver.find_element(By.XPATH,'//*[@id="j_username"]').send_keys("cpf") # manda usuario para o textfield
time.sleep(0.1) #ajax??
driver.find_element(By.XPATH,'//*[@id="btnLogin"]').click() # clica no botao



time.sleep(8) # espera carregar a pagina
driver.get(url_notas)
time.sleep(5) #esperar carregar a pagina



table_id = driver.find_element(By.XPATH, '//*[@id="resultado"]/center/table')  #seleciona tabela de notas
rows = table_id.find_elements(By.TAG_NAME, "tr") #seleciona as linhas da tabela e joga em uma lista de linhas


#abre stdout para escrever no arquivo
sys.stdout=open("saida.txt","a")

for row in rows[2:(len(rows)-1)]:    #começa do 2 e para no penultimo,pega a linha
     col = row.find_elements(By.TAG_NAME, "td")[0] # coluna do nome das materias ,td = coluna,tr = linha
     media = row.find_elements(By.TAG_NAME,"td")[2] #coluna de medias
     print (col.text + '              ' + media.text) 
  
sys.stdout.close() #fecga stdout
driver.quit() #fecha driver
