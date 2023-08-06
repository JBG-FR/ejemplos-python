

ppfr = 3.49
desc = 60 
ppnf = ppfr * (100 - desc) / 100
nupa = int(input("Ingrese el numero de panes que no son del día: "))
pnft = ppnf * nupa
print("El precio normal del pan es: " + str(ppfr) + "soles")
print("El descuento es de: " + str(desc) + " %")
print("El precio final es de: " + str(round(pnft,2)) + " soles")
