from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(f'La pagina fue abierta')
time.sleep(15)