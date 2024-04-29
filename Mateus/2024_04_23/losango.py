tamanho = int(input('Qual o tamanho do losango? '))
print(' ')
metade = tamanho // 2

if tamanho % 2 == 0:
    tamanho += 1
    print('Não é possível colocar um número par, logo será adicionado + 1 no desenho', tamanho)
    print('')

for altura in range(metade + 1):
    print(' ' * (metade - altura) + '+' * (2 * altura + 1))

for altura in range(tamanho):
    tamanho -= 2
    print(' ' * (altura + 1) + '+' * tamanho)