precio_normal = 3.49
descuento = 60  # 60%
barras_no_frescas = int(input("Ingrese el número de barras no frescas vendidas: "))
costo_total = barras_no_frescas * precio_normal * (1 - descuento / 100)
print("Precio habitual de una barra de pan: ${precio_normal:.2}")
print("Descuento por no ser fresca ({descuento}%): ${precio_normal * descuento / 100:.2}")
print("Costo final total: ${costo_total:.2}")
