#Per definire una funzione usrre def

#utilizzabile solo dopo avertla definita
#diIlMioNome()

def diIlMioNome():
    nome = input("Come ti chiami? ")
    print("Il tuo nome è: ", nome)

diIlMioNome()

#funzione con tipo di ritorno
#tipi dedotti in automatico dal compilatore
def addizione(a, b):
    risultato = a + b
    print("ho eseguito la funzione addizione")
    return risultato

x = addizione(1,1)
print(x)

x= addizione(1.1,1.2)
print(x)

#utilizzao della doctring
def media(valori):
    """
    Calcola la media dei valori nella lista fornita.

    Args:
        valori (list): una lista di numeri

    Returns:
        float: la media dei numeri nella lista
    """
    somma = 0
    for valore in valori:
        somma += valore
    media = somma / len(valori)
    return media

x= 11

def funzioneLocale():
    x=10
    print(x)

funzioneLocale()
print(x)


def funzioneGlobale():
    global y 
    y = 20
    print(y)
    return y

print(funzioneGlobale())
print(y)

