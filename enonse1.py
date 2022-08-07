# adres IP

adr=input("antre adres IP a: ")
pot=0

adr2= adr.split(".")
for i in adr2:
    for e in i:
        pot+=int(e)
pot=pot * int(adr[0])


print("Pot ki ouvri a se: ",pot)
