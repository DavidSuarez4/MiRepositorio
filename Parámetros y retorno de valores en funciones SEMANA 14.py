def calcular_descuento(montoDeCompra, porcentaje_descuento=10):
  descuento = montoDeCompra * porcentaje_descuento / 100
  return descuento


montoDeCompra = 10.0
descuento = calcular_descuento(montoDeCompra)

# Impresión del resultado
print(f"Monto total: ${montoDeCompra}")
print(f"Descuento (10%): ${descuento}")
print(f"Monto a pagar: ${montoDeCompra - descuento}")

# Ejemplo 2
montoDeCompra = 1000.0
porcentaje_descuento = 10
descuento = calcular_descuento(montoDeCompra, porcentaje_descuento)

# Impresión del resultado
print(f"\nMonto total: ${montoDeCompra}")
print(f"Descuento ({porcentaje_descuento}%): ${descuento}")
print(f"Monto a pagar: ${montoDeCompra - descuento}")
