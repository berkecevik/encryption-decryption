import collections
import random

class DES:
    INITIAL_PERMUTATION = [
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7,
        56, 48, 40, 32, 24, 16, 8, 0,
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6
    ]

    FINAL_SHUFFLE = [
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25,
        32, 0, 40, 8, 48, 16, 56, 24
    ]

    KEY_SELECTION = [
        48, 40, 32, 24, 16, 8, 0, 49,
        41, 33, 25, 17, 9, 1, 50, 42,
        34, 26, 18, 10, 2, 51, 43, 35,
        27, 19, 11, 3, 52, 44, 36, 28,
        20, 12, 4, 53, 45, 37, 29, 21,
        13, 5, 54, 46, 38, 30, 22, 14,
        6, 55, 47, 39, 31, 23, 15, 7
    ]

    KEY_COMPRESSION = [
        13, 16, 10, 23, 0, 4,
        2, 27, 14, 5, 20, 9,
        22, 18, 11, 3, 25, 7,
        15, 6, 26, 19, 12, 1,
        40, 51, 30, 36, 46, 54,
        29, 39, 50, 44, 32, 47,
        43, 48, 38, 55, 33, 52,
        45, 41, 49, 35, 28, 31
    ]

    EXPANSION_FUNCTION = [
        31, 0, 1, 2, 3, 4,
        3, 4, 5, 6, 7, 8,
        7, 8, 9, 10, 11, 12,
        11, 12, 13, 14, 15, 16,
        15, 16, 17, 18, 19, 20,
        19, 20, 21, 22, 23, 24,
        23, 24, 25, 26, 27, 28,
        27, 28, 29, 30, 31, 0
    ]

    P_SHUFFLE = [
        15, 6, 19, 20, 28, 11, 27, 16,
        0, 14, 22, 25, 4, 17, 30, 9,
        1, 7, 23, 13, 31, 26, 2, 8,
        18, 12, 29, 5, 21, 10, 3, 24
    ]

    SUB_BOX = [
        # S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        # S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 15, 2],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 7, 5, 14, 9, 0, 6, 12]
        ],
        # S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 15, 11, 1, 12],
            [13, 6, 8, 1, 15, 10, 3, 7, 9, 2, 5, 11, 12, 0, 14, 4],
            [7, 13, 14, 4, 3, 11, 2, 8, 1, 10, 15, 6, 9, 5, 0, 12]
        ],
        # S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 15, 11, 4, 12],
            [9, 7, 3, 5, 15, 13, 1, 10, 14, 0, 4, 8, 2, 11, 12, 6],
            [7, 11, 4, 1, 13, 14, 3, 15, 10, 2, 8, 12, 9, 5, 6, 0],
            [15, 0, 8, 14, 10, 6, 9, 3, 7, 4, 13, 12, 1, 5, 2, 11]
        ],
        # S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 10, 3, 15, 9, 8, 6, 0],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 14, 0],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        # S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 1, 8, 12, 7, 4, 10, 3, 11, 2, 13, 0, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 7, 8, 0, 11, 14, 1, 13, 6]
        ],
        # S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 9, 8, 0, 5, 6, 2],
            [14, 3, 4, 6, 2, 13, 8, 15, 12, 9, 1, 10, 7, 5, 11, 0]
        ],
        # S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 13, 6, 8, 15, 0, 3, 5, 10],
            [3, 13, 2, 8, 4, 6, 15, 11, 10, 1, 7, 9, 5, 0, 14, 12]
        ]
    ]

    def permute(self, bits, table):
        return [bits[i] for i in table]

    def xor(self, first, second):
        return [a ^ b for a, b in zip(first, second)]

    def sbox_lookup(self, bits):
        result = []
        for i in range(0, 48, 6):
            block = bits[i:i + 6]
            row = (block[0] << 1) | block[5]
            col = (block[1] << 3) | (block[2] << 2) | (block[3] << 1) | block[4]
            val = self.SUB_BOX[i // 6][row][col]
            result.extend([int(x) for x in f"{val:04b}"])
        return result

    def generate_subkeys(self, initial_key):
        key_bits = self.permute(initial_key, self.KEY_SELECTION)
        left, right = collections.deque(key_bits[:28]), collections.deque(key_bits[28:])
        subkeys = []

        for shift_count in [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]:
            left.rotate(-shift_count)
            right.rotate(-shift_count)
            combined_key = list(left) + list(right)
            subkey = self.permute(combined_key, self.KEY_COMPRESSION)
            subkeys.append(subkey)
        return subkeys

    def des_round(self, left_half, right_half, subkey):
        expanded_right = self.permute(right_half, self.EXPANSION_FUNCTION)
        xor_result = self.xor(expanded_right, subkey)
        sbox_output = self.sbox_lookup(xor_result)
        permuted_output = self.permute(sbox_output, self.P_SHUFFLE)
        return self.xor(left_half, permuted_output)

    def apply_initial_permutation(self, message_bits):
        return self.permute(message_bits, self.INITIAL_PERMUTATION)

    def apply_final_permutation(self, message_bits):
        return self.permute(message_bits, self.FINAL_SHUFFLE)

    def des_encrypt_block(self, plaintext_bits, subkeys):
        permuted_bits = self.apply_initial_permutation(plaintext_bits)
        left_half, right_half = permuted_bits[:32], permuted_bits[32:]

        for subkey in subkeys:
            new_left = right_half
            new_right = self.des_round(left_half, right_half, subkey)
            left_half, right_half = new_left, new_right

        combined = right_half + left_half
        return self.apply_final_permutation(combined)

    def des_decrypt_block(self, ciphertext_bits, subkeys):
        permuted_bits = self.apply_initial_permutation(ciphertext_bits)
        left_half, right_half = permuted_bits[:32], permuted_bits[32:]

        for subkey in reversed(subkeys):
            new_left = right_half
            new_right = self.des_round(left_half, right_half, subkey)
            left_half, right_half = new_left, new_right

        combined = right_half + left_half
        return self.apply_final_permutation(combined)

    def pad_message(self, message):
        padding_needed = 8 - (len(message) % 8)
        return message + chr(padding_needed) * padding_needed

    def remove_padding(self, padded_message):
        padding_amount = ord(padded_message[-1])
        return padded_message[:-padding_amount]

    def string_to_bits(self, text):
        return [int(bit) for char in text for bit in f"{ord(char):08b}"]

    def bits_to_string(self, bits):
        chars = [chr(int("".join(map(str, bits[i:i + 8])), 2)) for i in range(0, len(bits), 8)]
        return ''.join(chars)

    def des_encrypt(self, plaintext, key):
        padded_text = self.pad_message(plaintext)
        plaintext_bits = self.string_to_bits(padded_text)
        key_bits = self.string_to_bits(key)
        subkeys = self.generate_subkeys(key_bits[:56])

        encrypted_bits = []
        for i in range(0, len(plaintext_bits), 64):
            block = plaintext_bits[i:i + 64]
            encrypted_bits.extend(self.des_encrypt_block(block, subkeys))

        return ''.join(f"{bit}" for bit in encrypted_bits)

    def des_decrypt(self, ciphertext_bits, key):
        key_bits = self.string_to_bits(key)
        subkeys = self.generate_subkeys(key_bits[:56])

        decrypted_bits = []
        for i in range(0, len(ciphertext_bits), 64):
            block = [int(bit) for bit in ciphertext_bits[i:i + 64]]
            decrypted_bits.extend(self.des_decrypt_block(block, subkeys))

        decrypted_text = self.bits_to_string(decrypted_bits)
        return self.remove_padding(decrypted_text)

    def generate_random_key_des(self):
        return ''.join([str(random.randint(0, 1)) for _ in range(56)])