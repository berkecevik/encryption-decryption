
def mono_encrypt_tr(plain_mes, key, alphabet):
    cipher_mes = ''
    for i in plain_mes:
        if i.lower() in alphabet:
            index = alphabet.index(i.lower())
            cipher_char = key[index]
            cipher_mes += cipher_char.upper() if i.isupper() else cipher_char
        else:
            cipher_mes += i
    return cipher_mes


def mono_decrypt_tr(cipher_mes, key, alphabet):
    decrypted_mes = ''
    for i in cipher_mes:
        if i.lower() in key:
            index = key.index(i.lower())
            decrypted_char = alphabet[index]
            decrypted_mes += decrypted_char.upper() if i.isupper() else decrypted_char
        else:
            decrypted_mes += i
    return decrypted_mes

