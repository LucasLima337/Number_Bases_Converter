from time import sleep
from emoji import emojize
e = emojize(':arrow_forward:', use_aliases=True)
e1 = emojize(':fast_forward:', use_aliases=True)
n = int(input(f'\033[1;35m{e} Digite um número inteiro qualquer: '))
es = str(input(f'''{e} Escolha uma opção que deseja converter:
\033[1;32m[1] Binário
\033[1;33m[2] Octal
\033[1;34m[3] Hexadecimal \n\033[1;35m{e} Sua escolha: '''))
ba = cor = r = ''
print('')
if es == '1' or es == '2' or es == '3':
    print('\033[1;30mConvertendo...')
    sleep(1.60)
    print('')
    print('¨' * 40)
    if es == '1':
        ba = 'Binário'
        cor = '\033[1;32m'
        r = f'{n:b}'
    elif es == '2':
        ba = 'Octal'
        cor = '\033[1;33m'
        r = f'{n:o}'
    elif es == '3':
        ba = 'Hexadecimal'
        cor = '\033[1;34m'
        r = f'{n:x}'
    print(f'{e1} Base de conversão: {cor}{ba}\033[m')
    print(f'\033[1;30m{e1} Número Digitado: {cor}{n}\033[m')
    print(f'\033[1;30m{e1} Número convertido: {cor}{r}\033[m')
    print('\033[1;30m¨' * 40)
else:
    print('\033[1;31mDado inválido, tente novamente.\033[m')
