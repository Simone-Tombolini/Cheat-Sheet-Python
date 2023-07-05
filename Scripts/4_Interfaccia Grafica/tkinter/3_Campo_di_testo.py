import tkinter as tk


#definizione delle funzioni
#crea un testo
testo = ""

def ripeti():
    
    testo = testo_input.get()
    

    #scrivo su console
    print(testo)

    #creazione di iuna label
    testo_output = tk.Label(finestra, text=testo, fg="black", font=("Helvetica", 16))
    
    #posizionamento
    testo_output.grid(row=3, column=0)

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

#region bottone
#inserimento primo bottone
primoBottone = tk.Button(text="Ripeti!", command = ripeti)

#posizione in una griglia
primoBottone.grid(row=2, column=0, sticky= "W")
#endregion

testo_input = tk.Entry()
testo_input.grid(row=1, column=0, sticky="WE", padx=10)

#mount della finestra
if __name__ == "__main__":
    finestra.mainloop()

