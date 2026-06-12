import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("granizados.csv")

ventas_por_sabor = df.groupby("Sabor")["Ventas"].sum()

plt.figure(figsize=(8,5))
ventas_por_sabor.plot(kind="bar")

plt.title("Ventas por Sabor")
plt.xlabel("Sabor")
plt.ylabel("Cantidad de Ventas")

plt.tight_layout()
plt.show()