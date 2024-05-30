def eh_primo(valor:int) -> bool:
	if valor < 1:
		print("Valores negativos não são primos!")
		return False
	for i in range(2, valor):
		if valor % i == 0:
			print(valor, "não é um número primo!")
			return False
	print(valor, "é um número primo!")
	return True
valor = int(input("Digite um numero: "))
print(eh_primo(valor))
	