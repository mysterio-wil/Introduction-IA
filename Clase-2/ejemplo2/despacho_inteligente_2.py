# Datos en listas de diccionarios
pedidos = [
    {"ID": "O-702", "Pago": "Pendiente", "Stock": "Sí", "Destino": "Interior", "Peso": 7},
    {"ID": "O-708", "Pago": "Aprobado", "Stock": "Sí", "Destino": "Interior", "Peso": 10},
    {"ID": "O-705", "Pago": "Aprobado", "Stock": "No", "Destino": "Capital", "Peso": 2},
    {"ID": "O-701", "Pago": "Aprobado", "Stock": "Sí", "Destino": "Capital", "Peso": 3},
    {"ID": "O-703", "Pago": "Aprobado", "Stock": "Sí", "Destino": "Interior", "Peso": 8},
    {"ID": "O-707", "Pago": "Aprobado", "Stock": "Sí", "Destino": "Capital", "Peso": 6},
    {"ID": "O-704", "Pago": "Aprobado", "Stock": "Sí", "Destino": "Interior", "Peso": 12},
    {"ID": "O-706", "Pago": "Anulado", "Stock": "Sí", "Destino": "Capital", "Peso": 1},
]

# Función que aplica las reglas
def clasificar(pedido):
    pago = pedido["Pago"].lower()
    stock = pedido["Stock"].lower()
    destino = pedido["Destino"].lower()
    peso = pedido["Peso"]

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

# Clasificar pedidos
for pedido in pedidos:
    estado, metodo = clasificar(pedido)
    pedido["Estado"] = estado
    pedido["Metodo"] = metodo

# Mostrar resultados
print("Detalle por pedido:")
for pedido in pedidos:
    print(pedido)

# Contadores
from collections import Counter
estados = Counter(p["Estado"] for p in pedidos)
metodos = Counter(p["Metodo"] for p in pedidos if p["Metodo"])

print("\nRecuento por Estado:", estados)
print("Recuento por Método:", metodos)
