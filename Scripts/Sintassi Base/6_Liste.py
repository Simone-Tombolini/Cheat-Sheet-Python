#defininizione di una lista
lista = [2, "stringa", 1.11]
print(lista)
print(type(lista))
print(lista[1])

#sliceing
primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(primi[4:10])

#aggiungi un elemento alla lista
lista.append("aggiunto")

print(lista)

lista2 = [1,2, 3]

#unisci due liste
lista.extend(lista2)

print(lista)

#rimuovi l'iultimo elemneto
lista.pop()

#restituisce cosa hai levato
#il parametro è l'indice
elementoSalvato = lista.pop(3)
print(elementoSalvato)

print(lista)

#rimuovi la prima occorenza
#non la restituisce
lista.remove(2)

print(lista)

#per socrrere una lsita usare un for
for el in lista:
    print(el)

#funzioni per i tipi iterabili
print(max(primi))
print(sum(primi))


#enumerate
frutta = ["mela", "banana", "kiwi", "arancia"]
for indice, frutto in enumerate(frutta):
    print(indice, frutto)

#ordinamento

listaNonOridnata = [2,5,1,2,4]

#non modifica l'ordine dell'iterabile, ne restituisce uno nuovo iterato
copia = sorted(listaNonOridnata)

print(copia)
print(listaNonOridnata)

#modifica l'ordine dell'iterabile
listaNonOridnata.sort()
print(listaNonOridnata)

def pari(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#funzione filter
#filtra in base ad una funzione
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeriPari = list(filter(pari, numeri))
print(numeriPari)

def doppio(numero):
    return numero * 2

numeriDuplicati = list(map(doppio, numeri))
print(numeriDuplicati)



    

