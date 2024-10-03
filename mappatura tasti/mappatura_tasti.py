from pynput.keyboard import Listener

# Funzione che viene chiamata ogni volta che un tasto viene premuto
def premi(key):
    try:
        # Verifica se il tasto premuto è una lettera
        if key.char.isalpha():
            print(f'Tasto premuto: {key.char}')
    except AttributeError:
        # Ignora altri tasti che non sono lettere
        pass

# Avvia l'ascoltatore
with Listener(premio=premi) as listener:
    listener.join()