MOVE_ASCII = ord('a')
MOVE_ASCII_CAPITALISED = ord('A')


def vigenere_coding(text, key, decode=False):
    encrypted_text = []
    key_index = 0
    if decode:
        negative = -1
    else:
        negative = 1

    for char in text:
        if char.isalpha():
            move_value = ord(key[key_index % len(key)].lower()) - MOVE_ASCII
            if char.islower():
                encrypted_char = chr((ord(char) - MOVE_ASCII + move_value * negative) % 26 + MOVE_ASCII)
            else:
                encrypted_char = chr((ord(char) - MOVE_ASCII_CAPITALISED + move_value * negative) % 26 + MOVE_ASCII_CAPITALISED)
            key_index += 1
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)

    return ''.join(encrypted_text)


if __name__ == '__main__':
    decode = int(input('Szyfrowanie - 1, Deszyfrowanie - 2: '))
    test_text = input('Wprowadź tekst do zaszyfrowania i odszyfrowania używając szyfru Cezara: ')
    test_key = input('Wprowadź klucz (ciąg znaków): ')

    if decode == 1:
        encrypted_test_text = vigenere_coding(test_text, test_key)
        print('Zaszyfrowany tekst:', encrypted_test_text)
    elif decode == 2:
        decrypted_test_text = vigenere_coding(test_text, test_key, decode=True)
        print('Odszyfrowany tekst:', decrypted_test_text)
    else:
        raise ValueError('decode must be in range: 0 < decode < 3')
