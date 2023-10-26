# -*- coding: utf-8 -*-

def string_to_morse_code(x):
    """
    Returns the morse code of a string x.
    If x is not a string, returns 'ValueError, string expected!'.
    """

    mcode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
             'K': '-.-', 'L': '.-..', 'M': '--',   'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
             'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---',
             '3': '...--', '4': '....-',  '5': '.....',  '6': '-....',
             '7': '--...', '8': '---..',  '9': '----.',  '&': '.-...',
             "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
             ':': '---...', ',': '--..--', '=': '-...-',  '!': '-.-.--',
             '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.',
             '?': '..--..', '/': '-..-.'}

    if not isinstance(x, str):
        return "ValueError, string expected!"

    else:
        x=x.upper()
        # Change all the characters in the string uppercase
        # so it can be checked against the mcode
        morseString = ""
        for char in x:
            if char == " ":
                morseString += "x"
            else:
                morseString += mcode[char]
            morseString += "x"
        morseString = morseString[:len(morseString)-1]
        # removes the extra x at the end of the string

    return morseString
