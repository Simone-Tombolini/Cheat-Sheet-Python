import smtplib
#messaggio della mail
oggetto = "Subject: Urgente! da leggere subito!\n\n"
contenuto = "connettiti al Server che e meglio..."
messaggio = oggetto + contenuto
#definisci il serivzio
email = smtplib.SMTP("smtp.gmail.com", 587)

#connessione al server
email.ehlo()

#apertura canale criptato
email.starttls()

#per effettuare il login ricordarsi di abilitare dall'account google la verifica in due passaggi per la password
#seguire questa guida
#https://support.google.com/accounts/answer/185833
email.login("simone.tombolini@gmail.com", "kggrojzcznnuimlh")

#invia l'e-mail
email.sendmail("simone.tombolini@gmail.com", "simone.tombolini@gmail.com", messaggio)

#termina la connessione
email.quit()