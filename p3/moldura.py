frase = input('Digite a frase desejada: ')
ch = '\u2588'

for i in range(len(frase)+4):
    print(ch, end='')

print(f'\n{ch} {frase} {ch}')

for i in range(len(frase)+4):
    print(ch, end='')