#esercizio 4 Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore
Dizionario={"a": 1, "b": 2, "c": 3}
Dizionario2={}
for chiave, valore in Dizionario.items():
    Dizionario2[valore]=chiave
print(Dizionario2)