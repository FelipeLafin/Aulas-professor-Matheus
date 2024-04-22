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
            print('cadastro reprovado')
        else:
            input('Qual o regime? (mei, estagio, outro) ')
            if 'mei' and (sal > 6750):
                print('cadastro reprovado')
            elif 'estagio' and (est == 'n'):
                if(idade < 14) and (est == 'n'):
                    print('aprovado com ressalvas')
                elif(idade < 14) and (tr == 's'):
                    print('cadastro reprovado')
                else:
                    print('cadastro reprovado')
            elif 'outro':
                print('não é possível realizar o cadastro')
            elif (idade>=14 and idade <=16) and (tr == 's') and (est == 's'):
                print('aprovado com ressalvas')
            else:
                print('cadastro reprovado')
    else:
        if (idade >= 62) and (est == 'n'):
            print('aprovado com ressalvas')
        else:
            print('cadastro reprovado')