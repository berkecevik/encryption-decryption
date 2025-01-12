from key_generator import gcd
from key_generator import mod_inverse

def brute_force_affine_tr(cipher_mes, alphabet):
    possible_messages = []
    lengthOfAlphabet = len(alphabet)

    for a in range(1, lengthOfAlphabet):
        if gcd(a, lengthOfAlphabet) == 1:
            invA = mod_inverse(a, lengthOfAlphabet)
            if invA is None:
                continue

            for b in range(lengthOfAlphabet):
                plain_mes = ''
                for i in cipher_mes:
                    if i.upper() in alphabet:
                        y = alphabet.index(i)
                        decrypted_char_index = (invA * (y - b)) % lengthOfAlphabet
                        plain_mes += alphabet[decrypted_char_index]
                    else:
                        plain_mes += i
                possible_messages.append((a, b, plain_mes))

    return possible_messages
