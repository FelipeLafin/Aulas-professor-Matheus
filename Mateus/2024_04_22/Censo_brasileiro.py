print('------------------------------------------------------------------------------------------------------------------')
nome = input('Informe seu nome completo: ')
print('Dados de:', nome)
print('')
ano = int(input('Informe o seu ano de nascimento: '))
idade = (2024 - ano)
if (idade == 0) or (idade >150) or (ano > 2024):
    print('cadastro repovado')
else:
    print('Responda as perguntas abaixo com "s" para sim ou "n" para não')
    print('')
    est = (input('Você estuda? '))
    tr = (input('Você trabalha? '))
    if tr == 's':
        sal = int(input('Qual seu salário? '))
        if sal < 0:
            print('CADASTRO REPROVADO')
        else:
            input('Qual o regime? (mei, estagio, outro) ')
            if 'mei' and (sal > 6750):
                print('CADASTRO REPROVADO')
            elif 'estagio' and (est == 'n'):
                if(idade < 14) and (est == 'n'):
                    print('APROVADO COM RESSALVAS')
                elif(idade < 14) and (tr == 's'):
                    print('CADASTRO REPROVADO')
                else:
                    print('CADASTRO REPROVADO')
            elif 'outro':
                print('ERRO: Não é possível realizar o cadastro')
            elif (idade>=14 and idade <=16) and (tr == 's') and (est == 's'):
                print('APROVADO COM RESSALVAS')
            else:
                print('CADASTRO REPROVADO')
    else:
        if (idade >= 62) and (est == 'n'):
            print('APROVADO COM RESSALVAS')
        else:
            print('CADASTRO REPROVADO')
print('------------------------------------------------------------------------------------------------------------------')