#!/usr/bin/env python3

from itertools import starmap, cycle

def encrypt(message, key):
    message = filter(lambda _: _.isalpha(), message.upper())
    def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))
    return "".join(starmap(enc, zip(message, cycle(key))))

def decrypt(message, key):
    def dec(c,k): return chr(((ord(c) - ord(k)) % 26) + ord('A'))
    return "".join(starmap(dec, zip(message, cycle(key))))

if __name__=='__main__':
    inp = ''
    with open('enc.txt', 'r') as f:
        inp = f.read()
    key = 'A'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in letters:
        for j in letters:
            for k in letters:
                for l in letters:
                    key = f'{i}{j}{k}{l}'
                    dec = decrypt(inp, key)
                    freq = dec.count('THE')
                    if freq > 5:
                        print(f'--{key}: {freq}')
                        print(dec)


