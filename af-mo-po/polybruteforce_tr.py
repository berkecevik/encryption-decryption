import string
from poly_tr import poly_decrypt_tr

def poly_brute_force_tr(cipher_text, lenghtofalphabet):
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    possible_plain_texts = []
    key_lengths = [3]

    for key_length in key_lengths:
        for key in generate_possible_keys_tr(key_length, alphabet):
            decrypted_text = poly_decrypt_tr(cipher_text, key, alphabet)
            possible_plain_texts.append((key, decrypted_text))

    return possible_plain_texts

def generate_possible_keys_tr(length, alphabet):
    from itertools import product
    return [''.join(chars) for chars in product(alphabet, repeat=length)]