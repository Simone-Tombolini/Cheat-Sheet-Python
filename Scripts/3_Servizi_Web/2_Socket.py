import socket as sk
from os import *

#creazione client

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

#connettiamoci a google
#prima indirizzo dsn, poi porta, 80 default http
s.connect(("www.google.it", 80))

#restituisce la connessione
print(s)

#hostname su cui sto girando
ilMioNome = sk.gethostname()

print(ilMioNome)

#ip su cui sto girando
print(sk.gethostbyname(ilMioNome))

#ora posso fare chiamate rest

richiesta = "GET / HTTP/1.1\nHost: www.google.it\n\n"
# usiamo la funzione encode() per convertire la richiesta da stringa in
# bytes-object, in modo da poterla poi inviare al server:
s.send(richiesta.encode())

#ascoltiamo la risposta 20240 è la grandezza del buffer

#s.settimeout(5.0)
# finché c'è contenuto, len(risposta) sarà maggiore di zero.
risposta = s.recv(2048)
c= 0
while len(risposta)>0:
    
    print("nuovo clock")
    print(risposta)    
    risposta = s.recv(2048)
    system('cls')
    if not risposta:
        break
        

# output codice HTML homepage #
#ricordarsi di chiudere SEMPRE
s.close()
print("fine")