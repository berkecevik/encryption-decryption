from affine_en import affine_encrypt, affine_decrypt
from affine_tr import affine_encrypt_tr, affine_decrypt_tr
from defined_values import lenghtOfAlphabet, alphabetEN, alphabetTR, alphabet_tr
from key_generator import generate_affine_eng_key, generate_mono_eng_key, generate_poly_eng_key, generate_affine_tr_key, \
    generate_poly_tr_key, generate_mono_tr_key
from mono_en import mono_encrypt, mono_decrypt
from mono_tr import mono_encrypt_tr, mono_decrypt_tr
from poly_en import poly_encrypt, poly_decrypt
from poly_tr import poly_encrypt_tr, poly_decrypt_tr

with open("message.txt", "r", encoding="utf-8") as file:
    message = file.read().strip()

""" ### !!! AFFINE !!! ### """
a, b = generate_affine_eng_key()
encrypted_affine = affine_encrypt(message, a, b, lenghtOfAlphabet)
decrypted_affine = affine_decrypt(encrypted_affine, a, b,lenghtOfAlphabet)
print(f"Affine Key: {a, b}")
print(f"Encrypted Affine Text: {encrypted_affine}\n")
print(f"Decrypted Affine Text: {decrypted_affine}\n")

print("-----------------------------------")
""" ### !!! MONO ALPHABET !!! ### """
mono_key = generate_mono_eng_key()
encrypted_mono = mono_encrypt(message, mono_key, alphabetEN)
decrypted_mono = mono_decrypt(encrypted_mono, mono_key, alphabetEN)
print(f"Mono Key: {mono_key}")
print(f"Mono Encrypted: {encrypted_mono}\n")
print(f"Mono Decrypted: {decrypted_mono}\n")

print("-----------------------------------")

""" ### !!! POLY ALPHABET !!! ### """
poly_key = generate_poly_eng_key()
encrypted_poly = poly_encrypt(message, poly_key, lenghtOfAlphabet)
decrypted_poly = poly_decrypt(encrypted_poly, poly_key, lenghtOfAlphabet)
print(f"Poly Key: {poly_key}")
print(f"Poly encrypted: {encrypted_poly}\n")
print(f"Poly decrypted: {decrypted_poly}\n")
print("-----------------------------------")

"""AFFINE TR"""
a, b = generate_affine_tr_key()
encrypted_affine_tr = affine_encrypt_tr(message, a, b, alphabetTR)
decrypted_affine_tr = affine_decrypt_tr(encrypted_affine_tr, a, b, alphabetTR)
print(f"Affine Key TR:{a, b}")
print(f"Affine Encrypted TR:{encrypted_affine_tr}\n")
print(f"Affine Decrypted TR:{decrypted_affine_tr}\n")

print("-----------------------------------")
"""mono alphabet tr"""
mono_key_tr = generate_mono_tr_key()
encrypted_mono_tr = mono_encrypt_tr(message, mono_key_tr, alphabet_tr)
decrypted_mono_tr = mono_decrypt_tr(encrypted_mono_tr, mono_key_tr, alphabet_tr)
print(f"Mono Key TR: {mono_key_tr}")
print(f"Mono Encrypted TR: {encrypted_mono_tr}\n")
print(f"Mono Decrypted TR: {decrypted_mono_tr}\n")
print("-----------------------------------")

"""POLY ALPHABET TR"""
poly_key_tr = generate_poly_tr_key()
encrypted_poly_tr = poly_encrypt_tr(message, poly_key_tr, alphabet_tr)
decrypted_poly_tr = poly_decrypt_tr(encrypted_poly_tr, poly_key_tr, alphabet_tr)
print(f"Poly Key TR: {poly_key_tr}")
print(f"Poly Encrypted TR: {encrypted_poly_tr}\n")
print(f"Poly Decrypted TR: {decrypted_poly_tr}\n")




def save_to_file(filename, content, title):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{title}\n")
        file.write(content + "\n\n")

save_to_file("encrypted_affine.txt", encrypted_affine, "Encrypted Affine:")
save_to_file("decrypted_affine.txt", decrypted_affine, "Decrypted Affine:")
save_to_file("encrypted_affine.txt", encrypted_affine_tr, "Encrypted Affine TR:")
save_to_file("decrypted_affine.txt", decrypted_affine_tr, "Decrypted Affine TR:")

save_to_file("encrypted_mono.txt", encrypted_mono, "Encrypted MonoAlphabet:")
save_to_file("decrypted_mono.txt", decrypted_mono, "Decrypted MonoAlphabet:")
save_to_file("encrypted_mono.txt", encrypted_mono_tr, "Encrypted MonoAlphabet TR:")
save_to_file("decrypted_mono.txt", decrypted_mono_tr, "Decrypted MonoAlphabet TR:")

save_to_file("encrypted_poly.txt", encrypted_poly, "Encrypted PolyAlphabet:")
save_to_file("decrypted_poly.txt", decrypted_poly, "Decrypted PolyAlphabet:")
save_to_file("encrypted_poly.txt", encrypted_poly_tr, "Encrypted PolyAlphabet TR:")
save_to_file("decrypted_poly.txt", decrypted_poly_tr, "Decrypted PolyAlphabet TR:")