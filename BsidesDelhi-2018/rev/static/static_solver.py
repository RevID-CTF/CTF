enc = '?5b9no=k!5<jW;h7W~b4#|'
flag = ""
for i in range(len(enc)):
	tmp = ord(enc[i]) ^ 0xc
	if i & 1 == 0:
		tmp = tmp + 4
	else:
		tmp = tmp - 4
	flag += chr(tmp)
print flag[::-1]