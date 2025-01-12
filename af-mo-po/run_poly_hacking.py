from defined_values import lenghtOfAlphabet
from run import encrypted_poly
from polybruteforce import poly_brute_force

possible_decryptions = poly_brute_force(encrypted_poly, lenghtOfAlphabet)
for key, text in possible_decryptions:
    print(f"Attempt with key='{key}': {text}")