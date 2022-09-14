from morse_code import MORSE_CODE_DICT

string = input("Enter text and hit enter to translate to morse code: ")

words = string.split()

morse_code_list = []
for word in words:
    morse_word = ""
    for char in word:
        morse_word += f"{MORSE_CODE_DICT[char.upper()]} "
    morse_code_list.append(f"{morse_word}   ")

morse_string = (" ".join(morse_code_list)).strip()

print(morse_string)
