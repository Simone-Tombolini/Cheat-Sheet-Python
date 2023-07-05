import socket
import subprocess


def ricevi_comandi(conn):
    while True:
        try:
            richiesta = conn.recv(4096)
            risposta = 'Risposta: '
            if richiesta == b'CMD1':
                risposta += '1'
            elif richiesta ==b'CMD2':
                risposta += '2'
            else:
                risposta += 'bad request'
        
            data = risposta 
            conn.sendall(data.encode())
        except Exception as ex:
            print(str(ex))
            print("connessione interrotta")
            conn.close()
            break



def sub_server(indirizzo, backlog=1):
    try:
        s = socket.socket()
        s.bind(indirizzo)
        s.listen(backlog)
        print("Server Inizializzato. In ascolto...")
    except socket.error as errore:
        print(f"Qualcosa è andato storto... \n{errore}")
        print(f"Sto tentando di reinizializzare il server...")
        sub_server(indirizzo, backlog=1)
    conn, indirizzo_client = s.accept() #conn = socket_client
    print(f"Connessione Server - Client Stabilita: {indirizzo_client}")
    ricevi_comandi(conn)


if __name__ == '__main__':
    while True:
        sub_server(("", 20000))
    