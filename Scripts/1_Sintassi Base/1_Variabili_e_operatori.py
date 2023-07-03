#No dichiarazione 
x= 3
#Tipizzazione variabile automatica
pi = 3.14

#funzione type restituisce il tipo
print(type(x))

print(type(pi))

#isinstance restituisce un valore booleano se l'oggetto e il tipo sono uguali
print(isinstance(pi, int))

print(isinstance(pi, float))

#non valido
#print(isinstance(x, pi))

stirnga = "questa è una stringa"

print(stirnga)

stirngaEscape = "se voglio inserie i caratteri di escape uso lo slash come carattere \", se voglio iserirlo doppio slash \\ "

print(stirngaEscape)

#sezione cast
#per combinare una stringa con un numero serve un cast

frase = "il valore del pi greco è : "

#errore di sintassi
#frase = frase + pi

frase = frase + str(pi)

print(frase)

#input da tasitera tramite console

y = input()

print(y)

#puoi inserire un messaggio in fase di input

z = input("Metti un messaggio per l'input: ")

print(z)
