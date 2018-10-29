# converter

Disediakan web dimana kita bisa mengconvert format file ke format lain, sebagai contoh di web tersebut kita dapat mengubah format latex menjadi markdown. Terdapat cookie dalam bentuk hex yang menarik. Jika kita ubah cookienya maka akan terdapat pesan padding error. Disini kami menduga bahwa web kita dapat mengexploitasinya lebih lanjut dengan menggunakan teknik padding oracle attack.

Diatas merupakan kedua script yang kami gunakan untuk mendekripsi dan mengenkripsi cookie. Dengan decrypt.py kita dapat mendekripsi cookie dan dengan encrypt.py kita dapat mengenkripsi payload RCE yang menjadi ciphertext yang valid sebagai cookie.

Referensi : https://merricx.github.io/picoctf2018-padding-oracle/. sebagian script kami edit dari link tersebut, thanks to the author.
