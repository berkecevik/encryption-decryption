
def mono_encrypt(plain_mes, key, alphabet):
    cipher_mes = ''
    for i in plain_mes:
        if i.isalpha():
            index = alphabet.index(i.lower())
            cipher_mes += key[index]
        else:
            cipher_mes += i
    return cipher_mes


def mono_decrypt(cipher_mes, key, alphabet):
    plain_mes = ''
    for i in cipher_mes:
        if i.isalpha():
            index = key.index(i.lower())
            plain_mes += alphabet[index]
        else:
            plain_mes += i
    return plain_mes
