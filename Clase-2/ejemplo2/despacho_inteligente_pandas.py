import pandas as pd

# Datos
data = {
    "ID": ["O-702","O-708","O-705","O-701","O-703","O-707","O-704","O-706"],
    "Pago": ["Pendiente","Aprobado","Aprobado","Aprobado","Aprobado","Aprobado","Aprobado","Anulado"],
    "Stock": ["Sí","Sí","No","Sí","Sí","Sí","Sí","Sí"],
    "Destino": ["Interior","Interior","Capital","Capital","Interior","Capital","Interior","Capital"],
    "Peso": [7,10,2,3,8,6,12,1]
}

df = pd.DataFrame(data)

def classify(row):
    pago = row["Pago"].lower()
    stock = row["Stock"].lower()
    destino = row["Destino"].lower()
    peso = row["Peso"]

    if pago == "anulado":
        return "Anulado", None
    if pago != "aprobado":
        return "Pendiente", None
    if stock == "no":
        return "Enviado", None
    if destino == "capital" and peso <= 5:
        return "Enviado", "Moto"
    if destino == "interior" and peso <= 10:
        return "Enviado", "Correo"
    return "Enviado", "Expreso"

df[["Estado","Metodo"]] = df.apply(lambda r: pd.Series(classify(r)), axis=1)

print("Detalle por pedido:")
print(df)

print("\nRecuento por Estado:")
print(df["Estado"].value_counts())

print("\nRecuento por Método de envío (solo donde aplica):")
print(df["Metodo"].dropna().value_counts())
