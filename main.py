def string_to_morse(input_str):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    morse_code = ''
    for char in input_str.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char]
        else:
            morse_code += ''
    return morse_code.strip()


input_str = input("enter the string to convert into morse code:")
morse_code = string_to_morse(input_str)
print("morse code:", morse_code)
