
def poly_encrypt(plain_mes, key, lenghtOfAlphabet):
    cipher_mes = ''
    key_length = len(key)
    for i in range(len(plain_mes)):
        c = plain_mes[i]
        if c.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if c.islower():
                cipher_c = chr(((ord(c) - ord('a') + shift) % lenghtOfAlphabet) + ord('a'))
            else:
                cipher_c = chr(((ord(c) - ord('A') + shift) % lenghtOfAlphabet) + ord('A'))
        else:
            cipher_c = c
        cipher_mes += cipher_c
    return cipher_mes

def poly_decrypt(cipher_mes, key, lenghtOfAlphabet):
    plain_mes = ''
    key_lenght = len(key)
    for i in range(len(cipher_mes)):
        c = cipher_mes[i]
        if c.isalpha():
            shift = ord(key[i % key_lenght].lower()) - ord('a')
            if c.islower():
                plain_c = chr(((ord(c) - ord('a') - shift) % lenghtOfAlphabet) + ord('a'))
            else:
                plain_c = chr(((ord(c) - ord('A') - shift) % lenghtOfAlphabet) + ord('A'))
        else:
            plain_c = c
        plain_mes += plain_c
    return plain_mes

