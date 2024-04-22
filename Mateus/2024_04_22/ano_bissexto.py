ano = int(input('Digite um ano: '))
if ano % 4 == 0:
        print('O ano é bissexto')
else:
        proximo_ano = ano + (4 - ano % 4)
        print('O ano não é bissexto')
        print('O próximo ano bissexto será:', proximo_ano)