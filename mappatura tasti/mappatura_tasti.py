import pynput
from pynput import keyboard

def tasto_premuto(tasto):
    print(f'Hai premuto il tasto: {tasto}')

def tasto_rilasciato(tasto):
    if tasto == keyboard.Key.esc:
        print('STOP')
        return False
# Avvia il listener
with keyboard.Listener(on_press=tasto_premuto, on_release=tasto_rilasciato) as listener:
    print('Premi Esc per uscire.')
    listener.join()
