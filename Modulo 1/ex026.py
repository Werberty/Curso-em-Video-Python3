frase = str(input('Digite uma frase: ')).strip()
print('A leta A aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A primeira vez que ela parece é na {}º posição'.format(frase.lower().find('a') + 1))
print('E a ultima na {}º posição'.format(frase.lower().rfind('a') + 1))