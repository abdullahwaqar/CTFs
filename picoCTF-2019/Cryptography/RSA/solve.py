#!/usr/bin/env python3
# coding:utf-8
from math import gcd

def lcm(p, q):
  return (p * q) // gcd(p, q)

def generate_keys(p, q):
  N = p * q
  L = lcm(p - 1, q - 1)
  i = 0
  for i in range(2, L):
    if gcd(i, L) == 1:
      E = i
      break
  print(E)
  while True:
    if (i * L + 1) % E == 0:
      D = (i * L + 1) // E
      break
    i += 1
  print(D)
  return (E, N), (D, N)

def encrypt(plain_text, public_key):
  E, N = public_key
  plain_integers = [int(char,16) for char in plain_text]
  encrypted_integers = [pow(i, E, N) for i in plain_integers]
  encrypted_text = ''.join(chr(i) for i in encrypted_integers)
  return encrypted_text

def decrypt(encrypted_text, private_key):
  D, N = private_key
  # encrypted_integers = [ord(char) for char in encrypted_text]
  # #encrypted_integers = [encrypted_text]
  print(encrypted_text)
  encrypted_integers = [int(char,16) for char in encrypted_text]
  print(encrypted_integers)
  decrypted_intergers = [pow(i, D, N) for i in encrypted_integers]
  print(decrypted_intergers)
  decrypted_text = ''.join(str(i) for i in decrypted_intergers)
  return decrypted_text

def sanitize(encrypted_text):
  return encrypted_text.encode('utf-8', 'replace').decode('utf-8')

# Authenticated (unhashed) channel:
# n = 59883006898206291499785811163190956754007806709157091648869
# e = 65537
# c = 23731413167627600089782741107678182917228038671345300608183
# Encrypted channel:
# n = 165481207658568424313022356820498512502867488746572300093793
# e = 65537
# c = 150635433712900935381157860417761227624682377134647578768653

if __name__ == '__main__':
  public_key, private_key = generate_keys(192355607880290234740980693973, 311314068553039667905603427153)
  print(public_key)
  print(private_key)
  plain_text = hex(23731413167627600089782741107678182917228038671345300608183)[2:]
  # encrypted_text = encrypt(plain_text, public_key)
  # encrypted_text = encrypt([plain_text[i] for i in range(0, len(plain_text), 2)], public_key)
  encrypted_text = hex(150635433712900935381157860417761227624682377134647578768653)[2:]
  print(encrypted_text)
  # decrypted_text = decrypt(encrypted_text, private_key)
  decrypted_text = decrypt([encrypted_text[i]+encrypted_text[i+1] for i in range(0, len(encrypted_text)-1, 2)], private_key)

  print(f'''
秘密鍵: {public_key}
公開鍵: {private_key}

平文:
「{plain_text}」

暗号文:
「{sanitize(encrypted_text)}」

平文 (復号化後):
「{decrypted_text}」
'''[1:-1])




