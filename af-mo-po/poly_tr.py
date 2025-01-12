
def poly_encrypt_tr(plain_mes, key, alphabet):
    cipher_mes = ''
    key_length = len(key)
    lenghtofalphabet = len(alphabet)

    for i in range(len(plain_mes)):
        c = plain_mes[i]
        if c in alphabet:
            shift = alphabet.index(key[i % key_length])
            plain_index = alphabet.index(c)
            cipher_index = (plain_index + shift) % lenghtofalphabet
            cipher_mes += alphabet[cipher_index]
        else:
            cipher_mes += c
    return cipher_mes

def poly_decrypt_tr(cipher_mes, key, alphabet):
    plain_mes = ''
    key_lenght = len(key)
    lenghtofalphabet = len(alphabet)

    for i in range(len(cipher_mes)):
        c = cipher_mes[i]
        if c in alphabet:
            shift = alphabet.index(key[i % key_lenght])
            cipher_index = alphabet.index(c)
            plain_index = (cipher_index - shift) % lenghtofalphabet
            plain_mes += alphabet[plain_index]
        else:
            plain_mes += c
    return plain_mes

