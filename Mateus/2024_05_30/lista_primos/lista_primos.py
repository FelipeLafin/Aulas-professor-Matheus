def primo(valor: int) -> bool:
	if valor <= 1:
		return False
	for i in range(2,valor):
		if valor % i == 0:
			return False
	else:
		return True
def lista_primos(valor: int) -> list:
	lista = []
	for i in range(valor + 1):
		if primo(i):
			lista.append(i)
	return lista
n = int(input("Digite um numero maior que zero: "))
print(lista_primos(n))