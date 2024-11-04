MOVE_ASCII = ord('a')
MOVE_ASCII_CAPITALISED = ord('A')


def vigenere_encrypt(text, key):
    encrypted_text = []
    key_index = 0

    for char in text:
        if char.isalpha():
            move_value = ord(key[key_index % len(key)].lower()) - MOVE_ASCII
            if char.islower():
                encrypted_char = chr((ord(char) - MOVE_ASCII + move_value) % 26 + MOVE_ASCII)
            else:
                encrypted_char = chr((ord(char) - MOVE_ASCII_CAPITALISED + move_value) % 26 + MOVE_ASCII_CAPITALISED)
            key_index += 1
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)

    return ''.join(encrypted_text)


def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            move_value = ord(key[key_index % len(key)].lower()) - MOVE_ASCII
            if char.islower():
                decrypted_char = chr((ord(char) - MOVE_ASCII - move_value) % 26 + MOVE_ASCII)
            else:
                decrypted_char = chr((ord(char) - MOVE_ASCII_CAPITALISED - move_value) % 26 + MOVE_ASCII_CAPITALISED)
            key_index += 1
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)


if __name__ == '__main__':
    test_text = 'ARKADIUSZSTRAMKO'
    test_key = 'key'

    encrypted_test_text = vigenere_encrypt(test_text, test_key)
    print('Zaszyfrowany tekst:', encrypted_test_text)

    decrypted_test_text = vigenere_decrypt(encrypted_test_text, test_key)
    print('Odszyfrowany tekst:', decrypted_test_text)
