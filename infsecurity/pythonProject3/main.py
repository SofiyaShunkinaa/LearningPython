ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

BETTA_ROTOR = "LEYJVCNIXWPBQMDRTAKZGFUHOS"
ROTOR_VIII = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
ROTOR_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

REFLECTOR_B_DUNN = "AE-BN-CK-DQ-FU-GY-HW-IJ-LO-MP-RX-SZ-TV"

def setup_rotors(start_position):
    global BETTA_ROTOR, ROTOR_VIII, ROTOR_I
    betta_rotor = BETTA_ROTOR
    rotor_viii = ROTOR_VIII
    rotor_i = ROTOR_I

    betta_rotor = betta_rotor[-betta_rotor.index(start_position[0]):] + betta_rotor[:-betta_rotor.index(start_position[0])]
    rotor_viii = rotor_viii[-rotor_viii.index(start_position[1]):] + rotor_viii[:-rotor_viii.index(start_position[1])]
    rotor_i = rotor_i[-rotor_i.index(start_position[2]):] + rotor_i[:-rotor_i.index(start_position[2])]

    print(f"\nBETTA_ROTOR: {betta_rotor}")
    print(f"ROTOR_VIII: {rotor_viii}")
    print(f"ROTOR_I: {rotor_i}")
    print(f"REFLECTOR_B_DUNN: {REFLECTOR_B_DUNN}\n")

def press_key(input_letter):
    after_rotor_i = ROTOR_I[ALPHABET.index(input_letter)]
    after_rotor_viii = ROTOR_VIII[ALPHABET.index(after_rotor_i)]
    after_betta_rotor = BETTA_ROTOR[ALPHABET.index(after_rotor_viii)]

    index_in_reflector = REFLECTOR_B_DUNN.index(after_betta_rotor)
    if index_in_reflector == 0 or REFLECTOR_B_DUNN[index_in_reflector - 1] == '-':
        after_reflector_b_dunn = REFLECTOR_B_DUNN[index_in_reflector + 1]
    else:
        after_reflector_b_dunn = REFLECTOR_B_DUNN[index_in_reflector - 1]

    after_reverse_betta_rotor = BETTA_ROTOR[ALPHABET.index(after_reflector_b_dunn)]
    after_reverse_rotor_viii = ROTOR_VIII[ALPHABET.index(after_reverse_betta_rotor)]
    after_reverse_rotor_i = ROTOR_I[ALPHABET.index(after_reverse_rotor_viii)]

    change_rotor_position(BETTA_ROTOR, 3)
    change_rotor_position(ROTOR_VIII, 1)
    change_rotor_position(ROTOR_I, 3)

    return after_reverse_rotor_i

def change_rotor_position(rotor, step):
    rotor = rotor[step:] + rotor[:step]

def calculate_frequency(text, file_name):
    map_ = {}
    for c in text:
        map_[c] = map_.get(c, 0) + 1

    len_text = len(text)
    frequency_map = {}
    for key, value in map_.items():
        frequency_map[key] = value / len_text

    with open(file_name, 'w') as f:
        for key, value in sorted(frequency_map.items()):
            f.write(f"{key} - {value}\n")

if __name__ == "__main__":
    while True:
        start_position = input("Start position: ").upper()
        setup_rotors(start_position)
        input_text = input("Input text: ").upper()
        output_text = ''.join(press_key(letter) for letter in input_text)
        print("Output text:", output_text, "\n")

        calculate_frequency(input_text, "InFrequency.txt")
        calculate_frequency(output_text, "OutFrequency.txt")
