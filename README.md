# Morse Code Encoder

This is a simple GUI application to encode text to Morse code using Python and Tkinter.

## Features

- Encode text input to Morse code
- Display encoded Morse code
- Handles letters, numbers, punctuation and special characters
- Simple Tkinter GUI with entry field and encode button

## Code Overview

The code consists of:

- `MORSE_CODE_DICT` - Dictionary mapping characters to Morse code
- `convert_to_morse()` - Function to encode text to Morse code
- Tkinter GUI code - Simple input field, button and result label

### Morse Code Dictionary

The `MORSE_CODE_DICT` contains the mapping from characters to Morse code sequences. It supports letters, numbers, punctuation and some special Spanish characters.

### Encoding Function

The `convert_to_morse()` function takes the input text, loops through each character, looks up the Morse code in the dictionary and concatenates them into a string separated by spaces.

### Tkinter GUI

The Tkinter GUI is made up of:

- `msg_label` and `msg_entry` for the text input field
- `encode_btn` button to trigger encoding
- `output_label` to display the encoded Morse code

The `encode()` function is called when the encode button is clicked. It takes the text, converts to Morse code using `convert_to_morse()` and updates the `output_label`.

## Usage

Run the Python file and enter text in the input field. Click the "Codificar" button to encode the text to Morse code. The output will be displayed below.

## Installation

Requires Python 3 and Tkinter.

```
pip install tkinter
```
