dati = ["dato1", "dato2", "dato3"]

with open("File_Vuoto.txt","w") as file:
    
    file.write("Inizio file")

with open("File_Vuoto.txt","a") as file:
    
    for dato in dati:
        file.write(dato)
        file.write("\n")
        print(dato)