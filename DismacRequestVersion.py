import requests
import csv
from bs4 import BeautifulSoup
ofertas_table=[]
field_names=['Producto','Precio']
for i in range(1,13):
    url=f'https://www.dismac.com.bo/categorias/51-tecnologia.html?p={i}'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    for oferta in soup.select(".recent-slider .recent-container"):
        nombre=oferta.find("strong")
        if oferta.find("span",{"class":"bundle-price"}):
            precio = oferta.find("span", {"class": "price-currency bundle-price"})
        else:
            precio = oferta.find("span", {"class": "int"})

        ofertas_table.append([nombre.text.strip(), precio.text])
        print(nombre.text.strip(),"||",precio.text)

with open("DismacProductsAll.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.DictWriter(f, delimiter=',', fieldnames=field_names)
    writer.writeheader()
    writer = csv.writer(f,dialect="excel")
    writer.writerows(ofertas_table)

