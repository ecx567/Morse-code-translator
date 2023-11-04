import tkinter as tk

# Dictionary mapping characters to Morse code
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "+": ".-.-.",
    "$": "...-..-",
    "@": ".--.-.",
    "!": "-.-.--",
    "¡": "--...-",
    "¿": "..-.-",
}


# Function to convert text to Morse code
def convert_to_morse(text):
    cipher = ""
    for letter in text:
        if letter != " ":
            # Check if the letter is in the dictionary.
            if letter.upper() in MORSE_CODE_DICT:
                # gets the Morse code and concatenates it.
                cipher += MORSE_CODE_DICT[letter.upper()] + " "
        else:
            cipher += " "

    return cipher


# graphical interface in Tkinter

root = tk.Tk()
root.title("Codificador Morse")

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# Tag for input text
msg_label = tk.Label(main_frame, text="Ingrese el mensaje:")
msg_label.pack()

# Text input field
msg_entry = tk.Entry(main_frame)
msg_entry.pack(padx=20, pady=10)

# tag to show result
output_label = tk.Label(main_frame, text="", justify="left")
output_label.pack(padx=20, pady=10)


# Controller by clicking on the code button
def encode():
    message = msg_entry.get()
    morse = convert_to_morse(message)
    output_label.config(text=morse)


# button to encode
encode_btn = tk.Button(main_frame, text="Codificar", command=encode)
encode_btn.pack(pady=10)

root.mainloop()
