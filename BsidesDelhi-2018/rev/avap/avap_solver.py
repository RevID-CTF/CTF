enc = [97,107,102,96,124,51,116,88,98,51,50,126,88,51,116,88,54,115,88,96,52,115,116,122]

for i in range(255):
  tmp = "".join([chr(c ^ i) for c in enc])
  if "flag" in tmp:
    print tmp
    break