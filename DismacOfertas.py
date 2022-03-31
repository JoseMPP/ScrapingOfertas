import csv

from bs4 import BeautifulSoup
#Usando el archivo HTML del sitio web
file = r"D:\web\Practice\websiteswebsites\www.dismac.com.bo\categorias\51-tecnologia.html"

with open(file,encoding="utf-8") as f:
    html= f.read()

soup = BeautifulSoup(html,"html5lib")
table=[]
field_names=['Producto','Precio']
for oferta in soup.select(".recent-slider .recent-container"):
    nombre=oferta.find("strong")
    precio= oferta.find("span",{"class":"int"})
    table.append([nombre.text.strip(),precio.text])
    print(nombre.text.strip(),"||",precio.text)

with open("DismacProducts.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.DictWriter(f, delimiter=',', fieldnames=field_names)
    writer.writeheader()
    writer = csv.writer(f,dialect="excel")
    writer.writerows(table)

