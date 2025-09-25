# Datos de ejemplo
tabla = [
    {"ID": "O-502", "Pago": "Aprobado", "Stock": "Si"},
    {"ID": "O-506", "Pago": "Pendiente", "Stock": "No"},
    {"ID": "O-501", "Pago": "Aprobado", "Stock": "No"},
    {"ID": "O-505", "Pago": "Anulado", "Stock": "Si"},
    {"ID": "O-503", "Pago": "Pendiente", "Stock": "Si"},
    {"ID": "O-504", "Pago": "Aprobado", "Stock": "No"},
    {"ID": "O-508", "Pago": "Aprobado", "Stock": "No"},
    {"ID": "O-507", "Pago": "Aprobado", "Stock": "Si"},
]

contador = 0
lista_enviados = []

for fila in tabla:
    if fila["Pago"] == "Aprobado" and fila["Stock"] == "Si":
        contador += 1
        lista_enviados.append(fila["ID"])

print("Cantidad de pedidos enviados:", contador)
print("IDs enviados:", lista_enviados)
