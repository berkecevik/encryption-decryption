from key_generator import gcd
from key_generator import mod_inverse

def brute_force_affine(cipher_mes, lengthOfAlphabet):
    possible_messages = []

    for a in range(1, lengthOfAlphabet):
        if gcd(a, lengthOfAlphabet) == 1:
            invA = mod_inverse(a, lengthOfAlphabet)
            if invA is None:
                continue

            for b in range(lengthOfAlphabet):
                plain_mes = ''
                for i in cipher_mes:
                    if i.isalpha():
                        y = ord(i.lower()) - ord('a')
                        decrypted_char = (invA * (y - b)) % lengthOfAlphabet
                        plain_mes += chr(decrypted_char + ord('a'))
                    else:
                        plain_mes += i
                possible_messages.append((a, b, plain_mes))

    return possible_messages

