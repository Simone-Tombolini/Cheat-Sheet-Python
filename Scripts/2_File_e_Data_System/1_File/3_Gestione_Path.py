from pathlib import *


#stamoa il percorso di questo file
percorso = Path(__file__)
print("il percorso di questo file è: ")
print(percorso)

#stampa la cartella in cui sono
percorsoPadre = Path(__file__).parent
print("il percorso padre di questo file è: ")
print(percorsoPadre)

#stampa una lista di tutti i file nella cartella
#possibile specificare l'estensione
print(list(percorsoPadre.glob('*')))

#concatenare più di un percorso
percorsoFileDiTesto = percorsoPadre / "File_di_Testo.txt"
print("il percorso del file di testo nella cartella è: ")
print(percorsoFileDiTesto)

percorsoNonWindows = PurePath(__file__)

print(percorsoNonWindows)

percorsoWindows = PureWindowsPath(__file__)
print(percorsoWindows)