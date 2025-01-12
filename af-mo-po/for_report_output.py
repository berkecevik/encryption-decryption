from key_generator import generate_affine_eng_key,generate_affine_tr_key

a, b = generate_affine_eng_key()
print(f"Affine Key: {a, b}\n")

a, b = generate_affine_tr_key()
print(f"Affine Key TR:{a, b}")
