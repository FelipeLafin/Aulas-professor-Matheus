def soma_pares(lista: list, alvo: int) -> bool:
	for x in lista:
		for y in lista:
			if x + y == alvo:
				return True
	return False
print(soma_pares([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 3))