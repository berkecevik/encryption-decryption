"""Affine brute"""
from affinebruteforce import brute_force_affine
from defined_values import lenghtOfAlphabet
from run import encrypted_affine

possible_decryptions = brute_force_affine(encrypted_affine, lenghtOfAlphabet)
for a, b, message in possible_decryptions:
    print(f"Key (a={a}, b={b}): {message}")