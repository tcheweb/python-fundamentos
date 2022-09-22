# tenha uma tupla com várias palavras (sem acento)
#depois mostrar , para cada palavra, quais são as suas vogais
palavras = ('morango', 'goiaba', 'melancia', 'maca', 'banana', 'uva', 'abacate')
for palavra in palavras:
    print(f'\nAs vogais da palavra {palavra.upper()} são ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
