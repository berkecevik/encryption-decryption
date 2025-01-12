from defined_values import lenghtofalphabetTR
from run import encrypted_poly_tr
from polybruteforce_tr import poly_brute_force_tr


"""poly brute tr"""
possible_decryptions_tr = poly_brute_force_tr(encrypted_poly_tr, lenghtofalphabetTR)
for key, text in possible_decryptions_tr:
    print(f"Attempt with key='{key}': {text}")