from collections import Counter


POLISH_ALPHABET = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
POLISH_FREQUENCY = {  # https://pl.wikipedia.org/wiki/Alfabet_polski#Cz%C4%99sto%C5%9B%C4%87_wyst%C4%99powania_liter
    'a': 8.965, 'ą': 1.021, 'b': 1.482, 'c': 3.988, 'ć': 0.448, 'd': 3.293, 'e': 7.921,
    'ę': 1.131, 'f': 0.312, 'g': 1.377, 'h': 1.072, 'i': 8.286, 'j': 2.343, 'k': 3.411,
    'l': 2.136, 'ł': 1.746, 'm': 2.911, 'n': 5.600, 'ń': 0.185, 'o': 7.590, 'ó': 0.823,
    'p': 3.101, 'q': 0.003, 'r': 4.571, 's': 4.263, 'ś': 0.683, 't': 3.966, 'u': 2.347,
    'v': 0.034, 'w': 4.549, 'x': 0.019, 'y': 3.857, 'z': 5.620, 'ź': 0.061, 'ż': 0.885
}
ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ENGLISH_FREQUENCY = {  # https://en.wikipedia.org/wiki/Letter_frequency
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015,
    'h': 6.094, 'i': 6.966, 'j': 0.253, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749,
    'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758,
    'v': 0.978, 'w': 2.360, 'x': 0.250, 'y': 1.974, 'z': 0.074
}


def caesar_coding_with_alphabet(text, key, alphabet, decode=False):
    encrypted_text = []
    if decode:
        negative = -1
    else:
        negative = 1

    for char in text:
        char_lower = char.lower()
        if char_lower in alphabet:
            is_upper = char.isupper()
            idx = alphabet.index(char_lower)
            encrypted_char = alphabet[(idx + key * negative) % len(alphabet)]
            encrypted_text.append(encrypted_char.upper() if is_upper else encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


def get_frequency(text):
    text = text.lower()
    letter_occurrences = Counter([char for char in text if char.isalpha()])
    total_letters_count = sum(letter_occurrences.values())

    return {char: count / total_letters_count for char, count in letter_occurrences.items()}


def cracking_caesar(encrypted_text, alphabet, frequency, displayed_number=10):
    decryptions = []

    if displayed_number > 10 or displayed_number < 1:
        raise ValueError('displayed_number must be in range: 0 < displayed_number < 11')

    for key in range(len(alphabet)):
        decrypted_text = caesar_coding_with_alphabet(encrypted_text, key, alphabet, decode=True)
        freq_decrypted_text = get_frequency(decrypted_text)
        mean_squared_error = sum((freq_decrypted_text.get(char, 0) - frequency.get(char, 0)) ** 2 for char in frequency)
        mean_squared_error /= len(frequency)  # Normalize by the number of letters
        decryptions.append((mean_squared_error / 100, decrypted_text, key))
    decryptions.sort()

    return decryptions[:displayed_number]


if __name__ == '__main__':
    decode = int(input('Szyfrowanie + Deszyfrowanie - 1, Tylko Deszyfrowanie - 2: '))
    if decode == 1:
        test_text = input('Wprowadź tekst do zaszyfrowania używając szyfru Cezara i odszyfrowania metodą analizy częstotliwości: ')
        test_key = int(input('Wprowadź klucz szyfrujący (liczba): '))
    elif decode == 2:
        encrypted_test_text = input('Wprowadź tekst do odszyfrowania metodą analizy częstotliwości: ')
    language = int(input('Podaj język wprowadzonego tekstu (1 - Polski, 2 - Angielski): '))
    displayed_number = int(input('Wprowadź ilość obliczanych najbardziej prawdopodobnych kombinacji (od 1 do 10): '))

    if language == 1:
        if decode == 1:
            encrypted_test_text = caesar_coding_with_alphabet(test_text, test_key, POLISH_ALPHABET)
        decryptions = cracking_caesar(encrypted_test_text, POLISH_ALPHABET, POLISH_FREQUENCY, displayed_number)
    elif language == 2:
        if decode == 1:
            encrypted_test_text = caesar_coding_with_alphabet(test_text, test_key, ENGLISH_ALPHABET)
        decryptions = cracking_caesar(encrypted_test_text, ENGLISH_ALPHABET, ENGLISH_FREQUENCY, displayed_number)
    else:
        raise ValueError('language must be in range: 0 < language < 3')
    print(f'Zaszyfrowany tekst: {encrypted_test_text}\n')
    for score, decryption, key in decryptions:
        print(f"Klucz: {key}\n Rozszyfrowany tekst: {decryption}\n Błąd średniokwadratowy: {score:.4f}\n")
