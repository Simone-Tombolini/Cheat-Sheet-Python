import tkinter as tk

opzioni = ["mele", "pere", "banane", "anguria"]

#definizione delle funzioni

def cambia(parametro):
    #scrivo su console
    print(parametro)
    
    #modifica testo di una label
    testo_output.config(text = parametro)
    


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

testo_output = tk.Label(finestra, text="", fg="black", font=("Helvetica", 16))
testo_output.grid(row=1, column=0)

variable = tk.StringVar(finestra)
variable.set(opzioni[0]) # default value

dropDown = tk.OptionMenu(finestra, variable, *opzioni, command=cambia)
dropDown.grid(row=0, column=0, sticky= "W")

#mount della finestra
if __name__ == "__main__":
    finestra.mainloop()
    

