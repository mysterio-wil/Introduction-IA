# Lista de pedidos (igual que en tu tabla)
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

# Clasificación siguiendo tu pseudocódigo
for pedido in pedidos:
    pago = pedido["Pago"]
    stock = pedido["Stock"]
    destino = pedido["Destino"]
    peso = pedido["Peso"]

    if pago == "Anulado":
        pedido["Estado"] = "Anulado"
        pedido["Metodo"] = None
    elif pago != "Aprobado":
        pedido["Estado"] = "Pendiente"
        pedido["Metodo"] = None
    elif pago == "Aprobado" and stock == "No":
        pedido["Estado"] = "Enviado"
        pedido["Metodo"] = None
    elif pago == "Aprobado" and stock == "Sí":
        pedido["Estado"] = "Enviado"
        if destino == "Capital" and peso <= 5:
            pedido["Metodo"] = "Moto"
        elif destino == "Interior" and peso <= 10:
            pedido["Metodo"] = "Correo"
        else:
            pedido["Metodo"] = "Expreso"

# Mostrar resultados
print("Detalle por pedido:")
for p in pedidos:
    print(p)
