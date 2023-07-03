#la Logica booleana utilizza formati standard

#== operatore di uguaglianza

#= assegnameto

print(3 == 3)
print(3 != 4)
print(3>2) 

#If

x = 4
y = 5

#indentazioen fondamentale
if x == y:
    print("ramo true")
else:
    print("ramo false")
print("sono fuori dall'if")

x +=1

if x == y:
    print("ramo true")
else:
    print("ramo false")
print("sono fuori dall'if")

z = 0

if z<0:
    pass #non possiamo lasciare un blocco senza istruzioni, pass è un istruzioen che non fa nulla
elif z == 0:
    print("uguale")
else:
    print("maggiore")

#getsione e controlle degli input da tastiera

#se non metti un nuemro da errore in compilazione

numero = int(input("inserisci un numero intero: "))

print(type(numero))

if isinstance(numero, int):
    print("è effettivamente un nuemro")
else:
    print("non lo è, non dovresti mai entrare qui")

print("fine")