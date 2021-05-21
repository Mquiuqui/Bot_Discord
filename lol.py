from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

i = 0
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://br.op.gg/')





def buscar_contato(nick):
    campo_pesquisa = driver.find_element_by_xpath('//body/div[2]/div[2]/form[1]/input[1]')
    
    time.sleep(1)
    campo_pesquisa.click()
    time.sleep(1)
    campo_pesquisa.send_keys(nick)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(3)
    #driver.find_element_by_xpath("//button[@id='SummonerRefreshButton']").click()




def enviar_mensagem():
    time.sleep(3)
    Champ = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[4]/a[1]")
    Modo = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]")
    Tempo = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[5]")
    Resul = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]")

    kda1 = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]")
    kda2 = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/span[2]")
    kda3 = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/span[3]")

    championshow = Champ.text
    modoshow = Modo.text
    temposhow = Tempo.text
    resulshow = Resul.text
    kill = kda1.text
    death = kda2.text
    assist = kda3.text

    print("Champion : ",championshow) 
    print("Modos : ",modoshow) 
    print("Tempo de partida : ",temposhow) 
    print("Resultado : ",resulshow) 
    print("KDA : ",kill,"/",death,"/",assist) 

    driver.back()
    return [championshow,modoshow,temposhow,resulshow,kill,death,assist]

 

  



