#esercizio 3 calcolare il fattoriale di un numero
numero=int(input("inserisci un numero: "))
fattoriale=1
for i in range(1, numero+1):
    fattoriale=fattoriale*i
print(fattoriale)