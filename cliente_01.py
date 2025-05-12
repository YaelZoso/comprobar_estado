import requests
from time import sleep

server = "https://api.ejemplo.com/estado:5000"

for i in range(3):
    r = requests.get(f'{server}/')
    datos = r.text
    print(datos)
    sleep(1)
