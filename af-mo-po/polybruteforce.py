import string
from poly_en import poly_decrypt

def poly_brute_force(cipher_text, lenghtOfAlphabet):
    alphabet = string.ascii_lowercase
    possible_plain_texts = []
    key_lengths = [3]

    for key_length in key_lengths:
        for key in generate_possible_keys(key_length):
            decrypted_text = poly_decrypt(cipher_text, key, lenghtOfAlphabet)
            possible_plain_texts.append((key, decrypted_text))

    return possible_plain_texts

def generate_possible_keys(length):
    from itertools import product
    alphabet = string.ascii_lowercase
    return [''.join(chars) for chars in product(alphabet, repeat=length)]


