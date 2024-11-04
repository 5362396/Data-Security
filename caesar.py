MOVE_ASCII = ord('a')
MOVE_ASCII_CAPITALISED = ord('A')


def caesar_encrypt(text, key):
    encrypted_text = []

    for char in text:
        if char.isalpha():
            move_value = key % 26
            if char.islower():
                encrypted_char = chr((ord(char) - MOVE_ASCII + move_value) % 26 + MOVE_ASCII)
            else:
                encrypted_char = chr((ord(char) - MOVE_ASCII_CAPITALISED + move_value) % 26 + MOVE_ASCII_CAPITALISED)
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)

    return ''.join(encrypted_text)


def caesar_decrypt(encrypted_text, key):
    decrypted_text = []

    for char in encrypted_text:
        if char.isalpha():
            move_value = 26 - (key % 26)
            if char.islower():
                decrypted_char = chr((ord(char) - MOVE_ASCII + move_value) % 26 + MOVE_ASCII)
            else:
                decrypted_char = chr((ord(char) - MOVE_ASCII_CAPITALISED + move_value) % 26 + MOVE_ASCII_CAPITALISED)
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)


if __name__ == '__main__':
    test_text = 'ARKADIUSZSTRAMKO'
    test_key = 22

    encrypted_test_text = caesar_encrypt(test_text, test_key)
    print('Zaszyfrowany tekst:', encrypted_test_text)

    decrypted_test_text = caesar_decrypt(encrypted_test_text, test_key)
    print('Odszyfrowany tekst:', decrypted_test_text)
