#classe padre
class Persona:
    #costruttore
    def __init__(self, nome, cognome, età) -> None:
        #attributi
        self.nome = nome
        self.cognome = cognome
        self.età = età
    
    #metodi
    def CF(self):
        print(self.nome + self.cognome + str(self.età))

#creazione istanza
valentino = Persona("valentino", "rossi", 40)
valentino.CF()



class Studente(Persona):
    #variabli di classe
    oreSettimanali = 36

    totaleStudenti = 0

    #costruttore
    def __init__(self, nome, cognome, età , maticola):
        #attributi della classe definiti nel costurttore
        super().__init__(nome, cognome, età)
        self.matricola = maticola
        Studente.totaleStudenti +=1 #modifica per tutta la class
    
    def printMatricola(self):
        print(self.matricola)
    

print(Studente.totaleStudenti)

mario = Studente("mario", "rossi", 20, 12345)

#eredito i metodi
mario.CF()

print(Studente.totaleStudenti)

luigi = Studente("luigi", "rossi", 17, 12346)

print(Studente.totaleStudenti)

print(mario.nome)
print(mario.cognome)
print(mario.età)

mario.printMatricola()


print(mario.oreSettimanali)

#modifica la variablie di classe per la singola istanza
luigi.oreSettimanali +=4
print(luigi.oreSettimanali)


#costruttori altenrnativi



