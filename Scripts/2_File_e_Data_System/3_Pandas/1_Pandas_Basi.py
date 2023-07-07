import pandas as pd

#creazioe di una serie, per ora la labels è un indice numerico progressivo
a = [2,5,2]

serie = pd.Series(a)

print(serie)

#stampa come una lista, con gli indici 
print(serie[0])
#ora con indice creato a mano

serie2 = pd.Series(a, index=["a", "b", "c"])

print(serie2)

#se l'indice è personalizzato usa quello

print(serie2["b"])

#oppure da un dizionario

calorie = {"giorno 1": 420, "giorno 2": 380, "giorno 3": 390}
serie3 = pd.Series(calorie)
print(serie3)

#creazioen di un data frame, set di multi serie
#sono come array multi dimensionali
dataSet = {
  'Auto': ["BMW", "Volvo", "Ford"],
  'Numero': [3, 7, 2]
}

frame = pd.DataFrame(dataSet,index=["a", "b", "c"])

#stampi tutto
print(frame)

#solo un record, preso dall'indice
print(frame.loc["b"])

##solo un record, preso dal numero dell'indice
print(frame.iloc[1])

#stampa l'inizio
print(frame.head(2))

#e la fine
print(frame.tail(2))

#Le informazioeni utili
print(frame.info())
