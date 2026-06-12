import pandas as pd

df = pd.read_csv("granizados.csv")

print("Primeros datos:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())

print("\nValores nulos:")
print(df.isnull().sum())

print("\nDuplicados:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nCantidad de registros después de la limpieza:")
print(len(df))