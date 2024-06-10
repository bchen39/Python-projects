from Crypto.Cipher import AES
from Crypto.Util.Padding import pad as pkcs7_pad, unpad as pkcs7_unpad
import random

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    return zip(*[iter(iterable)]*n)

BYTE_ORDER:str = 'little'
LENGTH_PREFIX_BYTES:int = 4
BLOCK_SIZE:int = 16

KEY:bytes = b'qwertyuiQWERTYUI'
DEBUG:int = 0

"""
A function to encrypt a message `msg` using key `key` and IV `iv`
"""
def encrypt(plain_text:bytes, key:bytes, iv:bytes):
    padded_msg = pkcs7_pad(plain_text, BLOCK_SIZE)
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    cipher = cryptor.encrypt(padded_msg)
    return cipher

"""
A function to decrypt the cipher `cipher` using the key `key` and IV `iv`
"""
def decrypt(cipher:bytes, key:bytes, iv:bytes):
    s = cipher
    decryptor = AES.new(key,AES.MODE_CBC,iv)
    plaintext = decryptor.decrypt(s) 
    return plaintext

"""
`oracle` returns whether the `cipher` contains the correct padding.
NOTE: This is the padding oracle function.
"""
def oracle(cipher:bytes, iv:bytes) -> bool:
    decrypted = decrypt(cipher, KEY, iv)
    try:
        pkcs7_unpad(decrypted, BLOCK_SIZE)
        return True
    except ValueError:
        return False

"""
Attack time!
"""
def padding_oracle_attack_exploiter(cipher, iv):
    plain, cip_blocks, l = b'', [], len(cipher)

    # Break ciphertext into blocks.
    while (l > 0):
        cip_blocks.append(cipher[l - BLOCK_SIZE: l])
        l -= BLOCK_SIZE
    cip_blocks.append(iv)
    if DEBUG:
        print(cip_blocks)

    while(len(cip_blocks) >= 2):
        inter, plain_tmp, c1, c2, c0 = b'', b'', cip_blocks[0], cip_blocks[1], b''

        # Randomize our chosen ciphertext.
        for _ in range(BLOCK_SIZE - 1):
            c0 += random.randint(0, 255).to_bytes(1, 'little')
        for j in reversed(range(BLOCK_SIZE)):

            # Make sure the end of our chosen ciphertext matches padding.
            cip_known = b''
            for k in range(BLOCK_SIZE - 1 - j):
                cip_known += ((BLOCK_SIZE - j) ^ inter[k]).to_bytes(1, 'little')

            # Brute force until padding oracle doesn't output error.
            for i in range(256):
                c0 += i.to_bytes(1, 'little') + cip_known
                tmp = c0 + c1

                # With the right ciphertext, we can then find the intermediate value and thus the plaintext through the XOR operation.
                if (oracle(tmp, iv)):
                    inter = (c0[j]^(BLOCK_SIZE - j)).to_bytes(1, 'little') + inter
                    plain_tmp = (c0[j]^c2[j]^(BLOCK_SIZE - j)).to_bytes(1, 'little') + plain_tmp
                    break
                c0 = c0[:j]
            c0 = c0[:j - 1]
        cip_blocks = cip_blocks[1:]
        plain = plain_tmp + plain

    # Remove padding and output plaintext.
    print('Plaintext: ', pkcs7_unpad(plain, BLOCK_SIZE))


if __name__ == '__main__':
    iv = b'0000000000000000'
    # Test string
    p = b'This is cs528 padding oracle attack lab with hello world~~~!!'
    cipher = encrypt(p, KEY, iv)
    padding_oracle_attack_exploiter(cipher, iv)