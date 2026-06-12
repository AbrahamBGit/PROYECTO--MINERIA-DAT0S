import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("granizados.csv")

df["Sabor"] = df["Sabor"].astype("category").cat.codes
df["Tamaño"] = df["Tamaño"].astype("category").cat.codes

X = df[["Sabor", "Tamaño", "Precio"]]
y = df["Ventas"]

X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = RandomForestRegressor(random_state=42)

modelo.fit(X_entrenamiento, y_entrenamiento)

predicciones = modelo.predict(X_prueba)

error = mean_absolute_error(y_prueba, predicciones)

print("Error promedio:", error)