senha = 2463
t = 0
tM = 4
print('-----------------------------------------------------------------------------------------------')
while t < tM:
    SC = int(input('TYPE YOUR PASSWORD: '))
    if SC != 2463:
        print('Password incorrect')
        print('')
    else:
        print('Password correct')
        print('---------------------------------------------------------------------------------------------')
        break
    t += 1
if t == tM:
    print('TRY AGAIN IN 15 MINUTES')
    print('')
    print('GUESSES:', t)
    print('-----------------------------------------------------------------------------------------------')