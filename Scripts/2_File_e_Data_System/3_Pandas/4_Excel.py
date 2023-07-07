import pandas as pd
#py -m pip install openpyxl

#puoi leggere da un file
try:
  df = pd.read_excel('Data.xlsx', sheet_name="Sheet1")
  print(df)
except:
   print("foglio o file non trovato")
   
#data frame che uso come test
dataSet = {
  'Auto': ["BMW", "Volvo", "Ford"],
  'Numero': [3, 7, 2]
}

frame = pd.DataFrame(dataSet)

#a append
#w write
try:
    #se fallisce vuol dire che esiste già il foglio, e non lo crea nuovo
    with pd.ExcelWriter('Data.xlsx', mode="a") as writer:
      frame.to_excel(writer, sheet_name="Sheet2")
except:
    with pd.ExcelWriter('Data.xlsx', mode="w") as writer:
      frame.to_excel(writer, sheet_name="Sheet2")    

