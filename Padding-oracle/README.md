# Padding oracle attack

## Introduction

The padding oracle attack is a cryptographic side channel attack that takes advantage of the padding function’s outputs.

Firstly, let us discuss the CBC encryption and PKCS7 padding scheme. CBC breaks the plaintext into equal-sized blocks, padding the last part using some form of padding scheme: in this case the scheme is PKCS7, where you pad the remaining X values using the hex value of X. The first block is XOR’d with some initialization vector (IV), then encrypted using some key. The resulting ciphertext will be used as IV for the next block and so on.

The decryption essentially reverses the process: it decrypts the ciphertext, obtaining some intermediate value then XORs it with the previous ciphertext or the IV, obtaining the plaintext. However, when unpadding using PKCS7, the unpad function will output an error if the plaintext isn’t padded correctly. This can be exploited by an attacker by feeding arbitrary ciphertext to XOR with the intermediate value until a correct padding is obtained. Knowing the padding, the attacker can obtain the intermediate value and then the plaintext. 

For detailed steps please see my implementation.

## Run
```bash
pip install -r requirements.txt
python3 poa.py
```

You can change the test string to whatever you want.
