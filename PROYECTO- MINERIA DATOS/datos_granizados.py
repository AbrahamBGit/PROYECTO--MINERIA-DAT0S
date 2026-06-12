import pandas as pd
import random

sabores = ["Fresa", "Mango", "Limón", "Mora", "Piña"]
tamanos = ["Pequeño", "Mediano", "Grande"]

datos = []

for i in range(100):
    sabor = random.choice(sabores)
    tamano = random.choice(tamanos)
    precio = random.randint(5000, 12000)
    ventas = random.randint(20, 200)

    datos.append([sabor, tamano, precio, ventas])

df = pd.DataFrame(datos, columns=["Sabor", "Tamaño", "Precio", "Ventas"])

print(df.head())

df.to_csv("granizados.csv", index=False)

print("Archivo granizados.csv creado correctamente")