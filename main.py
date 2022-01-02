import pygame
import time

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound("sounds/sound.mp3")

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

text = input("Enter some text(English letters, numbers and punctuation): ").upper()
text = " ".join(text.split())   # Remove leading spaces

for char in text:   # Make sure that text only contains English letters, numbers, punctuation and spaces if not exit
    if char not in MORSE_CODE_DICT and char != " ":
        print("You can only Enter (English letters, numbers, punctuation and spaces).")
        exit(0)


morse_code_text = ""
for char in text:
    if char in MORSE_CODE_DICT:
        holder = MORSE_CODE_DICT[char]
    else:
        holder = "/"

    if len(morse_code_text) == 0:
        morse_code_text += holder
    else:
        morse_code_text += f" {holder}"

print(f"'{text}' in morse code  is: {morse_code_text}")

frequency = 400

for char in morse_code_text:
    if char == "-":
        sound.play(frequency, 700)
    elif char == ".":
        sound.play(frequency, 100)
    else:
        time.sleep(0.3)

    time.sleep(0.2)
