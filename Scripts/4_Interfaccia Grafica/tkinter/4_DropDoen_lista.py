import tkinter as tk

opzioni = ["mele", "pere", "banane", "anguria"]

#definizione delle funzioni




#region creazione finestra
#definizione della finestra
finestra = tk.Tk()

#grandezza
finestra.geometry("600x600")
#titolo
finestra.title("Prima finestra")
#possibilità di essere mofificata
finestra.resizable(False, False)
#colore della finestra
finestra.configure(background="white")
#endregion

testo_output = tk.Label(finestra, text="0000000000a", fg="black", font=("Helvetica", 16))
testo_output.grid(row=1, column=0)

variable = tk.StringVar(finestra)
variable.set(opzioni[0]) # default value

w = tk.OptionMenu(finestra, variable, *opzioni)
w.grid(row=0, column=0, sticky= "W")
tk.mainloop()



def ripeti(testo_output):
    #scrivo su console
    print(variable.get())

    #crea un testo
    
    #creazione di una label
    testo_output.config(text = "variable.get()")

#region bottone
#inserimento primo bottone
primoBottone = tk.Button(text="Saluta!", command = ripeti(testo_output))

#posizione in una griglia
primoBottone.grid(row=3, column=0, sticky= "W")
#endregion





#mount della finestra
if __name__ == "__main__":
    finestra.mainloop()
    

