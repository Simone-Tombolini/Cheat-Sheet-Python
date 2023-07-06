import textwrap
import pyodbc as db


#connessione ad un database
conn = db.connect('DRIVER={SQL Server};SERVER=DESKTOP-W10;DATABASE=test;UID=sa;PWD=hortus')
cursor = conn.cursor()

#Eseguire una select
cursor.execute("select * from Tabella1")
rows = cursor.fetchall()#prende tutti i risultati
#verranno stampate in una lista
print(str(rows))
#Eseguire una select
n = 1
cursor.execute("select * from Tabella1 where Campo1 = ?", n)
rows = cursor.fetchone()#prende solo il primo risultato
#verranno stampate in una lista
print(str(rows))
#eseguire una select con dei parametri

#eseguire una insert, prima usando la rollback
cursor.execute("INSERT INTO Tabella1 (Campo1, Campo2) VALUES (1, 'prova sbagliata')")
conn.rollback()#annulla le modifiche non committate

#ora la faccio giusta
cursor.execute("INSERT INTO Tabella1 (Campo1, Campo2) VALUES (0, 'prova insert')")
conn.commit()#invia al database i dati


#stampa tutti i campi con i parametri di una tabella
for row in cursor.columns(table='Tabella1'):
    print (row.column_name)
    for field in row:
        print (field)

#serve per ottenere informazioni, usa intellisense per capire cosa ti da come opzioni
print(conn.getinfo(db.SQL_DATABASE_NAME))

#chiudi la connessione
conn.close()