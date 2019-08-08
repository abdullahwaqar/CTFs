enc = open('enc.txt', 'rb').read().split(' ')

flag = ''
for c in enc:
    flag += chr(int(c))

print(flag)
