"""affine brute tr"""
from affinebruteforce_tr import brute_force_affine_tr
from defined_values import alphabetTR
from run import encrypted_affine_tr

possible_messages = brute_force_affine_tr(encrypted_affine_tr, alphabetTR)
for a, b, message in possible_messages:
    print(f"Key (a={a}, b={b}): {message}")