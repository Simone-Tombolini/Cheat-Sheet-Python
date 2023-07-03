#importa la libreria
import tkinter as tk

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

#mount della finestra
if __name__ == "__main__":
    finestra.mainloop()
