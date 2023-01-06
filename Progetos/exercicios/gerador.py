from random import randint

resultado = [0] * 7   # posição 0 não será usada.
for i in range(100):
    x = randint(1,6)
    resultado[x] += 1
    
for i in range(1, 7):
    print(i, ": ", resultado[i])