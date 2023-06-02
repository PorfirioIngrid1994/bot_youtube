from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class RoboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def busca(self, busca, paginas):
        videos = []
        pagina = 1

        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.webdriver.get(url)
        time.sleep(5) 

        while pagina <= paginas:
            titulos = self.webdriver.find_elements(By.XPATH, "//a[@id='video-title']")
            for titulo in titulos:
                print('Vídeo encontrado: %s' % titulo.text)
            pagina += 1

    def proxima_pagina(self):
        pass


bot = RoboYoutube()
bot.busca("lontras", 5)
time.sleep(5)
