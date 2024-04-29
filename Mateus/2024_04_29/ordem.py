import random
lista = []
for i in range(0, 10):
    lista.append(random.randint(0, 10))
print('Lista antes: ',lista)

l = len(lista)
for i in range(l):
    for d in range(l - 1):
        if lista[d] > lista[d + 1]:
            temp = lista[d]
            lista[d] = lista[d + 1]
            lista[d + 1] = temp
print ('nova lista: ', lista)