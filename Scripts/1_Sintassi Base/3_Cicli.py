#ciclo while

contatore = 0
while contatore <=10:
    print(contatore)
    contatore +=1

#istruzioen break

while True:
    x=int(input("inserisci 0 per terminare il ciclo"))
    print("esegui quello che vuoi qui")
    if x == 0:
        break

print("fine del ciclo con break")

#il do-while non è supportato nativamente, utilizzare un construtto di questo tipo

while True:
    y = input("inserisci 0 per terminare il ciclo")
    print("esegui quello che vuoi qui")
    if y == 0:
        break

contatore = 0

while contatore < 10:
    contatore += 1
    if contatore == 5:
        print("Sto saltando " + str(5))
        continue
    print(contatore)

#attenzione a dove viene messo il contatore
contatore = 0
while contatore <=10:
    if contatore == 5:
         print("entro nel ciclo infinito")
         continue
    print(contatore)
    contatore +=1
    #questa istrunzione serve per continuare con la compilazione
    if(contatore == 100):
        break

#Ciclo for
#diverso da tutti i linguaggi che conosciamo di norma
#importante la funzione range
#è composta da range(punto di inizio, punto di fine, quantità del passo)
for numero in range(11):
    print(numero)
   
for numero in range(2, 11, 2):
    print(numero)

for numero in range(10, -1, -1):
    print(numero)


