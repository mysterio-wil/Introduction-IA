import pandas as pd

# Crear DataFrame con los pedidos
data = {
    "ID": ["O-502", "O-506", "O-501", "O-505", "O-503", "O-504", "O-508", "O-507"],
    "Pago": ["Aprobado", "Pendiente", "Aprobado", "Anulado", "Pendiente", "Aprobado", "Aprobado", "Aprobado"],
    "Stock": ["Si", "No", "No", "Si", "Si", "No", "No", "Si"]
}

df = pd.DataFrame(data)

# Filtrar pedidos enviados (Pago aprobado y Stock sí)
enviados = df[(df["Pago"] == "Aprobado") & (df["Stock"] == "Si")]

# Mostrar resultados
print("Pedidos enviados:")
print(enviados)
print("\nCantidad de pedidos enviados:", len(enviados))
