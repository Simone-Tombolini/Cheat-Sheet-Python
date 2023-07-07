import pandas as pd


df = pd.read_csv('dati_corrotti.csv')
#con il to srting stampa tutto
print(df)

#con questo se c'è una cella vcon valore null viene eliminato
df =  df.dropna()

print(df)

#con questo riempo tutte le celle null
df = df.fillna(999)

print(df)

#cosi solo con la prima colonna rimpiazzo
df["Calories"].fillna(999, inplace= True)#inplace fa si che il dataframe si modiifchi e non ritorni una copia

print(df)

#cerca su tutte le durate, se è maggiore di 120, rimpiazza
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df)

#cerca su tutte le durate, se è maggiore di 110, rimpiazza
for x in df.index:
  if df.loc[x, "Duration"] > 110:
    df.drop(x , inplace = True)

print(df)
print("prova")


