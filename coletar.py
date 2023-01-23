"""
acessar página local 10.10.10.210 e coletar dados biometria
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def pagina_acesso(endereco):
    driver.get(endereco)

def login(user, password):
    driver.find_element_by_xpath('//*[@id="lblLogin"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="lblPass"]').send_keys(password)
    time.sleep(5)

def seleciona_eventos(data_incial, data_final):
    driver.find_element_by_xpath('//*[@id="dvREP"]/div/div[3]/a').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="divMenuEvents"]/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="menuItem2"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="lblDataI"]').send_keys(Keys.CONTROL + 'a')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="lblDataI"]').send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath('//*[@id="lblDataI"]').send_keys(data_incial)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="lblDataF"]').send_keys(Keys.CONTROL + 'a')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="lblDataF"]').send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath('//*[@id="lblDataF"]').send_keys(data_final)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="communication"]/table/tbody/tr[5]/td/a').click()
    time.sleep(35)

def sair_pagina():
    driver.find_element_by_xpath('//*[@id="exitBtn"]/span').click()
    time.sleep(2)
    driver.close()
