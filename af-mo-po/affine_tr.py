from key_generator import mod_inverse

def affine_encrypt_tr(plain_mes, a, b, alphabet):
    cipher_mes = ''
    lenghtofalphabet = len(alphabet)

    for i in plain_mes:
        if i.upper() in alphabet:
            x = alphabet.index(i.upper())
            encrypted_char_index = (a * x + b) % lenghtofalphabet
            cipher_mes += alphabet[encrypted_char_index]
        else:
            cipher_mes += i
    return cipher_mes

def affine_decrypt_tr(cipher_mes, a, b, alphabet):
    plain_mes = ''
    lenghtofalphabet = len(alphabet)
    invA = mod_inverse(a,lenghtofalphabet)

    for i in cipher_mes:
        if i.upper() in alphabet:
            y = alphabet.index(i.upper())
            decrypted_char_index = (invA * (y - b)) % lenghtofalphabet
            plain_mes += alphabet[decrypted_char_index]
        else:
            plain_mes += i
    return plain_mes.lower()

