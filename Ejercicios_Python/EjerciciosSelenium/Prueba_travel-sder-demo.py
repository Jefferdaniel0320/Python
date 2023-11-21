import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

url = ""
gionB = "_"
gionM = "-"
fechaSalida = str(input("Fecha de Salida AAAAMMDD: "))
fechaRegreso = str(input("Fecha de Regreso AAAAMMDD: "))
origen = str(input("Origen: "))
destino = str(input("Destino: "))
textoclase = str(input("marca b para business, e para economy, p para premiumEconomy: "))

if textoclase == "b":
    clase = "business"
elif textoclase == "e":
    clase = "economy"
elif textoclase == "p":
    clase = "premiumEconomy"

adult = str(input("adult: "))
child = str(input("child: "))
infant = str(input("infant: "))
fechaTotal = fechaSalida + gionB + origen + gionB + destino + gionM + fechaRegreso + gionB + destino + gionB + origen
pasajeros = adult + "_adult/" + child + "_child/" + infant + "_infant"

url = "https://travel-sder-demo.smartlinks.dev/flights/availability/round/" + fechaTotal + "/all/" + clase + "/all-stops/domestic/" + pasajeros
print(url)
input("Oprime Enter para seguir")

driver = webdriver.Chrome()
driver.get(url)
print('Pantalla abierta')

input('Se cumplio el ciclo de acceso, oprime Enter para que termine el programa... ')

driver.quit()
