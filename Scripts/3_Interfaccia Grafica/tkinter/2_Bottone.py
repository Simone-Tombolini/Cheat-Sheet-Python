import tkinter as tk

#definizione delle funzioni

def saluta():
    #scrivo su console
    print("ciao")

    #crea un testo
    testo = "Hello World!"
    
    #creazione di iuna label
    testo_output = tk.Label(finestra, text=testo, fg="black", font=("Helvetica", 16))
    
    #posizionamento
    testo_output.grid(row=1, column=0)

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

#inserimento primo bottone
primoBottone = tk.Button(text="Saluta!", command = saluta)

#posizione in una griglia
primoBottone.grid(row=0, column=0, sticky= "W")

#mount della finestra
if __name__ == "__main__":
    finestra.mainloop()

