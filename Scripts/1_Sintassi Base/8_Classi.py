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

    @classmethod
    def StudenteDaStringa(cls, stringa):
        nome, cognome, età , maticola = stringa.split(",") 
        return cls(nome, cognome, età , maticola)
    @staticmethod
    def somma(a,b):
        print(a+b)
    
    #ridefinizione deglio operatori

    def __add__(self, altro):
        """ Solo per fini didattici. Usare i dunder in maniera intelligente! """
        return self.nome + " " + altro.cognome
    
    def __str__(self):
        return "Studente : " + self.nome + " " + self.cognome
    
    def __repr__(self):
        return "Studente : " + self.nome + " " + self.cognome + " " + str(self.età) + " " + str(self.matricola) 


print(Studente.totaleStudenti)

mario = Studente("mario", "rossi", 20, 12345)

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

maria = Studente.StudenteDaStringa("maria,rossi,22,12347")

maria.printMatricola()

maria.somma(3,3)
print(str(maria))
print(repr(maria))
