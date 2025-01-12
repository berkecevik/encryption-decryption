from des import DES

with open("message.txt", "r", encoding="utf-8") as file:
    message = file.read().strip()

des_system = DES()
key = des_system.generate_random_key_des()
cipher_mes = des_system.des_encrypt(message, key)
des_key = des_system.generate_random_key_des()

print(f"DES Key: {des_key}")
print(f"Encrypted: {cipher_mes}")
decrypted_mes = des_system.des_decrypt(cipher_mes, key)
print(f"Decrypted: {decrypted_mes}")

def save_to_file(filename, content, title):
    with open(filename, 'a') as file:
        file.write(f"{title}\n")
        file.write(content + "\n\n")

save_to_file("encrypted_message.txt", cipher_mes, "Encrypted with DES:")
save_to_file("decrypted_message.txt", decrypted_mes, "Decrypted with DES:")