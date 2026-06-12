import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("granizados.csv")

df["Sabor"] = df["Sabor"].astype("category").cat.codes
df["Tamaño"] = df["Tamaño"].astype("category").cat.codes

X = df[["Sabor", "Tamaño", "Precio"]]
y = df["Ventas"]

X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42
)

parametros = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10, None]
}

modelo = RandomForestRegressor(random_state=42)

grid = GridSearchCV(
    modelo,
    parametros,
    cv=5,
    scoring="neg_mean_absolute_error"
)

grid.fit(X_entrenamiento, y_entrenamiento)

print("Mejores parámetros:")
print(grid.best_params_)