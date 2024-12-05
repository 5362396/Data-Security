P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]

IP = [2, 6, 3, 1, 4, 8, 5, 7]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
P4 = [2, 4, 3, 1]
IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]


def permute(bits, table):
    return [bits[i - 1] for i in table]


def split(bits):
    middle = len(bits) // 2
    return bits[:middle], bits[middle:]


def left_shift(bits, shift):
    return bits[shift:] + bits[:shift]


def generate_keys(key):
    # Step 1: We accepted a 10-bit key and permuted the bits by putting them in the P10 table.
    permuted_key = permute(key, P10)
    # Step 2: We divide the key into 2 halves of 5-bit each.
    l, r = split(permuted_key)
    # Step 3: Now we apply one bit left-shift on each key.
    l, r = left_shift(l, 1), left_shift(r, 1)
    # Step 4: Combine both keys after step 3 and permute the bits by putting them in the P8 table. The output of the given table is the first key K1.
    k1 = permute(l + r, P8)
    # Step 5: The output obtained from step 3 i.e. 2 halves after one bit left shift should again undergo the process of two-bit left shift.
    l, r = left_shift(l, 2), left_shift(r, 2)
    # Step 6: Combine the 2 halves obtained from step 5 and permute them by putting them in the P8 table. The output of the given table is the second key K2.
    k2 = permute(l + r, P8)
    return k1, k2


def s_box(bits, sbox):
    row = (bits[0] << 1) | bits[3]
    col = (bits[1] << 1) | bits[2]
    return [int(i) for i in format(sbox[row][col], '02b')]


def complex_function(bits, key):
    # After the initial permutation, we get an 8-bit block of text which we divide into 2 halves of 4 bit each.
    l, r = split(bits)
    # On the right half, we perform expanded permutation using EP table which converts 4 bits into 8 bits.
    expanded_permutation_output = permute(r, EP)
    # We perform XOR operation using the first key K1 with the output of expanded permutation.
    xor_output = [i ^ j for i, j in zip(expanded_permutation_output, key)]
    # We take the first and fourth bit as row and the second and third bit as a column for our S boxes.
    s0 = s_box(xor_output[:4], S0)
    s1 = s_box(xor_output[4:], S1)
    # S boxes gives a 2-bit output which we combine to get 4 bits and then perform permutation using the P4 table.
    p4_output = permute(s0 + s1, P4)
    # We XOR the output of the P4 table with the left half of the initial permutation table i.e. IP table.
    # We combine both halves i.e. right half of initial permutation and output of ip.
    return [i ^ j for i, j in zip(l, p4_output)] + r


def s_des_encrypt(text, key):
    k1, k2 = generate_keys(key)
    # Step-1: We perform initial permutation on our 8-bit plain text using the IP table.
    permuted_text = permute(text, IP)
    # Step-2
    first_fk = complex_function(permuted_text, k1)
    # Step-3: Now, divide the output into two halves of 4 bit each. Combine them again, but now the left part should become right and the right part should become left.
    swap = first_fk[4:] + first_fk[:4]
    # Step-4: Again perform step 2, but this time while doing XOR operation after expanded permutation use key 2 instead of key 1.
    second_fk = complex_function(swap, k2)
    # Step-5: Perform inverse initial permutation. The output of this table is the cipher text of 8 bit.
    return permute(second_fk, IP_INVERSE)


if __name__ == '__main__':
    test_text = [1, 0, 0, 1, 1, 0, 0, 1]
    test_key = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

    print(s_des_encrypt(test_text, test_key))
