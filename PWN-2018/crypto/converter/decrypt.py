from requests import *

url = "http://converter.uni.hctf.fun/show"
vals = "a2ce888edc74c4520e2f7a32f554e6580c7c16bc7e502ecaa06784f5be2fca0f66d0140ce3e5c735cae276688af4a7b6d15e33ceb5915b5234e453639fe21818"

def is_valid_padding(ct_hex):
    cookie = {"vals": ct_hex}
    r = get(url, cookies=cookie)
    ret =  "ValueError: Invalid padding bytes." not in r.text
    print("Padding : {} = {}".format(ct_hex, ret))
    return ret

iv = vals[:2*16]
ct = [vals[i:i+32] for i in range(0, len(vals), 32)]
#ct = ct[:2]
print(len(ct))

original_block = []
for c in ct:
    original_block.append(c.decode('hex'))

print(is_valid_padding(vals))
raw_input()
pt = ''
for n_block in range(len(original_block)-2,-1,-1):
    zero_byte = 15
    pad_str = ord('\x01')
    inter_state = []
    pad_bytes = ''
    for i in range(16):
        print('Guessing [{}] bytes...'.format(15-i))
        for j in range(0, 256):
            guess_c2 = ('0'*zero_byte + chr(j) + pad_bytes).encode('hex')
            payload = iv + guess_c2 + ct[-1]
            if is_valid_padding(payload):

                temp = chr(pad_str ^ ord(original_block[n_block][zero_byte]) ^ j)
                inter_state.append(temp)

                print('Found plaintext :', temp.encode('hex'))

                pt = temp + pt
                pad_bytes = ''
                for k in range(i+1):
                    pad_bytes += chr((pad_str+1) ^ ord(original_block[n_block][15-k]) ^ ord(inter_state[k]))
                pad_bytes = pad_bytes[::-1]
                break

        pad_str += 1
        zero_byte -= 1
        print('PLAINTEXT so far {}'.format(pt.encode('hex')))
        raw_input("")

    print('Moving to the prev block..')
    del ct[-1]

print('Decrypted: {}'.format(pt))
