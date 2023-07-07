import pandas as pd

df = pd.read_csv('pokedex.csv')
#con il to srting stampa tutto
print(df.to_string())

#se il dataframe supera il numero di righe massimo stampa solo le prime e utile 5
print(df)
print(pd.options.display.max_rows) 

#data frame che uso come test
dataSet = {
  'Auto': ["BMW", "Volvo", "Ford"],
  'Numero': [3, 7, 2]
}

df2 = pd.DataFrame(dataSet)

df2.to_csv('nuovo_CSV.csv', index= False)