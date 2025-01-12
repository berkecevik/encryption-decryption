import random
import string

def gcd(a, b):
    while b !=0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if(a * x) % m == 1:
            return x
    return None


def generate_affine_eng_key():
    a = random.randint(1,25)
    while gcd(a, 26) !=1:
        a = random.randint(1, 25)
    b = random.randint(0, 25)
    return a,b
def generate_affine_tr_key():
    a = random.randint(1, 28)
    while gcd(a, 29) != 1:
        a = random.randint(1, 28)
    b = random.randint(0, 28)
    return a, b


def generate_mono_eng_key():
    alphabetEN = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabetEN)
    return ''.join(alphabetEN)
def generate_mono_tr_key():
    alphabetTR = list("abcçdefgğhıijklmnoöprsştuüvyz")
    random.shuffle(alphabetTR)
    return''.join(alphabetTR)


def generate_poly_eng_key(length=3):
    return''.join(random.choice(string.ascii_lowercase)
                  for _ in range(length))
def generate_poly_tr_key(length=3):
    alphabetTR = list("abcçdefgğhıijklmnoöprsştuüvyz")
    return''.join(random.choice(alphabetTR)
                  for _ in range(length))


