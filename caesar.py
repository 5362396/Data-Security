MOVE_ASCII = ord('a')
MOVE_ASCII_CAPITALISED = ord('A')


def caesar_coding(text, key, decode=False):
    encrypted_text = []

    for char in text:
        if char.isalpha():
            if decode:
                move_value = 26 - (key % 26)
            else:
                move_value = key % 26
            if char.islower():
                encrypted_char = chr((ord(char) - MOVE_ASCII + move_value) % 26 + MOVE_ASCII)
            else:
                encrypted_char = chr((ord(char) - MOVE_ASCII_CAPITALISED + move_value) % 26 + MOVE_ASCII_CAPITALISED)
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)

    return ''.join(encrypted_text)


if __name__ == '__main__':
    decode = int(input('Szyfrowanie - 1, Deszyfrowanie - 2: '))
    test_text = input('Wprowadź tekst do zaszyfrowania i odszyfrowania używając szyfru Cezara: ')
    test_key = int(input('Wprowadź klucz (liczba): '))

    if decode == 1:
        encrypted_test_text = caesar_coding(test_text, test_key)
        print('Zaszyfrowany tekst:', encrypted_test_text)
    elif decode == 2:
        decrypted_test_text = caesar_coding(test_text, test_key, decode=True)
        print('Odszyfrowany tekst:', decrypted_test_text)
    else:
        raise ValueError('decode must be in range: 0 < decode < 3')
