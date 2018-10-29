from requests import *

url = "http://converter.uni.hctf.fun/show"
vals = "a2ce888edc74c4520e2f7a32f554e6580c7c16bc7e502ecaa06784f5be2fca0f66d0140ce3e5c735cae276688af4a7b6d15e33ceb5915b5234e453639fe21818"

def is_valid_padding(ct_hex):
    cookie = {"vals": ct_hex}
    r = get(url, cookies=cookie)
    ret =  "ValueError: Invalid padding bytes." not in r.text
    print("Padding : {} = {}".format(ct_hex, ret))
    return ret

def xor(s1, s2):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

def str_replace(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def pad(s):
    bs = 16
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

new = '{"f":"b","c":"","t":";/bin/cat *"}'
new = pad(new)

target = [new[i:i+16] for i in range(0, len(new), 16)]

iv = vals[:2*16]

block  = [iv.decode('hex')]
block += ['0'*16]*(len(target) - 1)
block += ['A'*16]

for n_block in range(len(block)-2,-1,-1):
    for i in range(16):
        print 'Guessing [{}]-byte'.format(15-i)
        for j in range(0,256):
            block[n_block] = str_replace(block[n_block], 15-i, chr(j))

            ciphertext = (block[n_block]+block[n_block+1]).encode('hex')
            payload = iv + ciphertext
            if is_valid_padding(payload):
                for k in range(i+1):
                    if i == 15:
                        break
                    new_val = chr(ord(block[n_block][15-k]) ^ (i+1) ^ (i+2))
                    block[n_block] = str_replace(block[n_block], 15-k, new_val)
                print 'FOUND valid ciphertext:', ciphertext
                break

        print 'Moving to previous bytes...'

    print 'Flipping to desired plaintext...'
    block[n_block] = xor(block[n_block], '\x10'*16)
    block[n_block] = xor(block[n_block], target[n_block])
    print("Ciphertext now {}".format(''.join(block).encode('hex')))

print(repr(new))
print 'Final ciphertext:', ''.join(block).encode('hex')
