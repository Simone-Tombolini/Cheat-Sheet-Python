from functools import wraps
#crea il decoratore
def aggiungiIntestazione(funzione):
    #serve per non perdere le informaizoni della funzione originle sostituendola con wrapper
    @wraps(funzione)
    #wrapper che sarà l'aggiunta alla funzione
    def wrapper():
        #cose da aggiungere alla funzione, eseguite prima 
        print("eseguzione della funzione: ")
        print(funzione.__name__)
        #
        funzione()
        print("fine eseguzione della funzione: ")
        print(funzione.__name__)
    return wrapper

def aggiungiIntestazioneConParametro(funzioneConParametro):
    @wraps(funzioneConParametro)
    def wrapper(*args, **kwargs):

        print("eseguzione della funzione: ")
        print(funzioneConParametro.__name__)

        funzioneConParametro(*args, **kwargs)
        
        print("fine eseguzione della funzione: ")
        print(funzioneConParametro.__name__)

    return wrapper

@aggiungiIntestazione
def funzioneTest1():
    print("hello world")

funzioneTest1()

@aggiungiIntestazioneConParametro
def funzioneTest2(parametro):
    print(parametro)

funzioneTest1()
funzioneTest2("stringa")