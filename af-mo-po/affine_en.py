from key_generator import mod_inverse


def affine_encrypt(plain_mes, a, b, lenghtOfAlphabet):
    cipher_mes = ''
    for i in plain_mes:
        if i.isalpha():
            x = ord(i.upper()) - ord('A')
            encrypted_char = (a * x + b) % lenghtOfAlphabet
            cipher_mes += chr(encrypted_char + ord('A'))
        else:
            cipher_mes += i
    return cipher_mes

def affine_decrypt(cipher_mes, a, b, lenghtOfAlphabet):
    plain_mes = ''
    invA = mod_inverse(a,lenghtOfAlphabet)
    for i in cipher_mes:
        if i.isalpha():
            y = ord(i.lower()) - ord('a')
            decrypted_char = (invA * (y - b)) % lenghtOfAlphabet
            plain_mes += chr(decrypted_char + ord('a'))
        else:
            plain_mes += i
    return plain_mes
