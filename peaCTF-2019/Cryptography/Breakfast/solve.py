# Note: https://en.wikipedia.org/wiki/Bacon%27s_cipher

chiper = open('enc.txt', 'rb').readlines()[0]

spl = ''

for char in chiper:
    if char == '0' or char == '1':
        spl += char
    if len(spl) == 5:
        print(spl)
        spl = ''
