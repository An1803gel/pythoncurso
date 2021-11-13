#Declarar variables
mes = input("Escribe el mes: ")
dias = float(input("¿Cuantos dias laboraste? "))
pagoxdia = float(input("¿Cual es tu pago por dia? "))

#Procedimiento
pagobruto = dias * pagoxdia
ivat = pagobruto * .16
subtotal = pagobruto + ivat
ivar = 2 * ivat / 3
isr = pagobruto * 0.10
pagon = subtotal - ivar - isr

#Resultados

print ("Mes de ", mes)
print ("Dias trabajados ", dias)
print ("Paga por dia = ", pagoxdia)

print ("Pago bruto= ", pagobruto) 
print ("IVA trasladado= ", ivat)
print ("Subtotal ", subtotal)
print ("IVA retenido= ", ivar)
print ("ISR retenido= ", isr)
print ("Pago neto= ", round(pagon, 2))