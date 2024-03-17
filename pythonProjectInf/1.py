import math

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def calculate_entropy(letters, length):
    entropy = 0
    sum_p = 0
    for letter in letters:
        p = letters[letter] / length
        print(f"Amount of ({letter}): {letters[letter]} | P({letter}) -> {p}")

        if 0 < p <= 1:
            entropy += -1 * p * math.log2(p)
        else:
            print(f"Invalid value for letter {letter}: {p}")

        sum_p += p

    print("\nSum of p: " + str(sum_p) + '\n')
    return entropy


def calculate_hartly_entropy(length):
    return math.log2(length)

def calculate_amount_info_with_mistake(message, entropy, p):
    if 0 < p < 1:
        return len(message) * (entropy - (-p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)))
    elif p == 1.0:
        print(f"Invalid probability value: {p}. Setting result to 0.")
        return 0
    else:
        print(f"Invalid probability value: {p}")
        return 0



def process_alphabet(text, alphabet):
    letters = {}
    length_of_message = 0
    symbols = 0

    for char in text:
        if char in alphabet:
            length_of_message += 1
            if letters.get(char) is None:
                letters[char] = 0
                symbols += 1
            else:
                letters[char] += 1

    print("Text length without others symbols:", length_of_message)
    print("Amount of unique symbols in text:", symbols, '\n')

    return letters, length_of_message, symbols


print('Task 1-a. Latin alphabet\n')

latin_text = read_file('latin.txt').lower()
latin_letters, latin_length, latin_symbols = process_alphabet(latin_text, 'abcdefghijklmnopqrstuvwxyz')

e_s = calculate_entropy(latin_letters, latin_length)
e_h = calculate_hartly_entropy(latin_symbols)

print("Shannon Entropy (Latin):", e_s)
print("Hartley Entropy (Latin):", e_h)
print('\n--------------------------------------------------------------------------------------------------\n\n\n')


print('Task 1-b. Cyrillic alphabet\n')

cyrillic_text = read_file('cyrillic.txt').lower()
cyrillic_letters, cyrillic_length, cyrillic_symbols = process_alphabet(cyrillic_text, 'абвгдежзийклмнопрстуфхцчшщъыьэюя')

e_s_c = calculate_entropy(cyrillic_letters, cyrillic_length)
e_h_c = calculate_hartly_entropy(cyrillic_symbols)

print("Shannon Entropy (Cyrillic):", e_s_c)
print("Hartley Entropy (Cyrillic):", e_h_c)
print('-----------------------------------------------------------------------------------------------------------------\n')


print('Task 2. Binary alphabet\n')

binary_text = '01001000011001010110110001101100011011110010110000100000010101110110111101110010011011000110010000100001'
binary_digits, bin_length_message, symbols = process_alphabet(binary_text, '01')

bin_e_s = calculate_entropy(binary_digits, bin_length_message)
print('Binary alphabet entropy:', bin_e_s)

print('\n---------------------------------------------------------------------------------------------------------------\n\n')


print('Task 3. Amount of Information\n')

FIO = "Shunkina Sofiya Dzmitrievna"
ascii_FIO = "".join(str(ord(char)) for char in FIO)

print("FIO:", FIO)
print("ASCII FIO:", ascii_FIO, '\n')


amount_FIO_info = e_s * len(FIO)
amount_ascii_FIO_info = bin_e_s * len(ascii_FIO)

print(f'Amount of information -> message: "{FIO}" = {amount_FIO_info} bit')
print(f'Amount of information -> message: "{ascii_FIO}" = {amount_ascii_FIO_info} bit')

print('\n---------------------------------------------------------------------------------------------------------------\n\n')


print('Task 4. Amount of Information with mistakes\n')

mistake1 = 0.1
mistake2 = 0.5
mistake3 = 1.0

print(f'Amount of information (p={mistake1}): {calculate_amount_info_with_mistake(FIO, bin_e_s, mistake1)} bit')
print(f'Amount of information (p={mistake2}): {calculate_amount_info_with_mistake(ascii_FIO, bin_e_s, mistake2)} bit')
print(f'Amount of information (p={mistake3}): {calculate_amount_info_with_mistake(ascii_FIO, bin_e_s, mistake3)}')


