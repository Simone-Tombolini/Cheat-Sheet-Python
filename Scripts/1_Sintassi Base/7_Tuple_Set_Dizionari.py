tupla = (1,2,3)
#le tuple sono immutabili

print(tupla)
#vietato tupla.append()

set= {1,1,1,1,1,2,3}
#i set non perettono duplicati

print(set)

#dizionari
#lista composta da coppie chiave valori

dizionario = {"chiave1" : "valore", "chiave2": 2}

print(type(dizionario))
print(dizionario)

dizionario["chiave2"] = "nuovo valore"

print(dizionario)

#contorollare se c'è la chiave
print("chiave1" in dizionario)

#restiriusico tutte le chiavi
print(dizionario.keys())

#restiriusico tutti i valori
print(dizionario.values())

#restituisco le coppie in una lista di tuple
print(dizionario.items())

#Packing e unpacking

for key, value in dizionario.items():
    print(key, value)

def funz():
    return 1,2

print(funz())

v1,v2 = funz()
print(v1)
print(v2)

def funz2(*args):
    print(args)

funz2(1,2,3,4,5)

def funz3(**kwargs):
    print(kwargs)

funz3(nome = "mario", cogome= "rossi")



