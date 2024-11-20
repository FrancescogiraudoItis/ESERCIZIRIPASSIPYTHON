import socket
from pynput import keyboard  # Utilizzeremo questa libreria per intercettare i tasti premuti

# Indirizzo del server e porta
server_address = ("192.168.1.131", 12345)  # Indirizzo IP e porta del server
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connessione al server
tcp_client_socket.connect(server_address)

print("Premi un tasto per inviarlo al server (P per uscire)...")

# Flag per tenere traccia dello stato di invio dei comandi
sending = False

# Funzione per gestire la pressione dei tasti
def on_press(key):
    global sending
    try:
        key_pressed = key.char  # Ottieni il carattere del tasto premuto
    except AttributeError:
        key_pressed = str(key)  # Usa il nome del tasto se non è un carattere (es. 'Key.space')

    if not sending:
        print(f"Tasto premuto: {key_pressed}")
        
        # Invia il tasto al server
        tcp_client_socket.send(key_pressed.encode('utf-8'))
        sending = True  # Inizia a inviare comandi

    # Esci se viene premuto il tasto 'p'
    if key_pressed == "p":
        print("Chiusura del client...")
        tcp_client_socket.close()
        return False  # Interrompi il listener e chiudi il programma

# Funzione per gestire il rilascio dei tasti
def on_release(key):
    global sending
    try:
        key_released = key.char  # Ottieni il carattere del tasto rilasciato
    except AttributeError:
        key_released = str(key)  # Usa il nome del tasto se non è un carattere (es. 'Key.space')
    
    print(f"Tasto rilasciato: {key_released}")
    
    # Invia il carattere 'x' al server quando il tasto viene rilasciato
    tcp_client_socket.send('x'.encode('utf-8'))
    
    sending = False  # Interrompi l'invio dei comandi quando il tasto viene rilasciato

# Avvia il listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Chiudi il socket alla fine (nel caso il client non sia chiuso da 'p')
tcp_client_socket.close()
