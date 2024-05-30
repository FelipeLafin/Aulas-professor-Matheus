def validador_parenteses(s: str) -> bool:
	for x in s:
		contador = 0
		if "(" in s:
			contador +=1
		else:
			contador -=1
		if ")" in s:
			contador +=1
		else:
			contador -=1
	if contador >=1:
		return True
	else:
		return False

# Valores válidos
print(validador_parenteses('()'))
print(validador_parenteses('()()'))
print(validador_parenteses('(())'))
print(validador_parenteses('(()()())'))
print(validador_parenteses('(((())()))'))

# Valores inválidos
print(validador_parenteses(')'))
print(validador_parenteses('('))
print(validador_parenteses('()('))
print(validador_parenteses('()()())'))
print(validador_parenteses('(((())())'))