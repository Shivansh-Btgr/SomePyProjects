import tkinter as tk
from tkinter import messagebox


def text_to_morse(text):
    text_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': '/'
    }
    
    words = text.upper().split()
    translated_morse = ''
    
    for word in words:
        letters = list(word)
        for letter in letters:
            translated_morse += text_dict.get(letter, '') + ' '
        translated_morse += '/ '
    
    return translated_morse.strip()

def morse_to_text(morse_code):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '-----': '0', '/': ' ', '': ''
    }
    
    words = morse_code.split(' / ')
    translated_text = ''
    
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            translated_text += morse_dict.get(letter, '')
        translated_text += ' '
    
    return translated_text.strip()


def translate():
    selected_option = option_var.get()
    input_text = input_entry.get()
    if selected_option == 1:
        translated_text = morse_to_text(input_text)
        messagebox.showinfo("Translation Result", f"Morse to Text:\n{translated_text}")
    elif selected_option == 2:
        translated_morse = text_to_morse(input_text)
        messagebox.showinfo("Translation Result", f"Text to Morse:\n{translated_morse}")
    else:
        messagebox.showerror("Error", "Invalid option selected.")
window = tk.Tk()
window.title("Morse Code Translator")
option_label = tk.Label(window, text="Select Translation Option:")
option_label.pack()
option_var = tk.IntVar()
morse_to_text_radio = tk.Radiobutton(window, text="Morse to Text", variable=option_var, value=1)
morse_to_text_radio.pack()
text_to_morse_radio = tk.Radiobutton(window, text="Text to Morse", variable=option_var, value=2)
text_to_morse_radio.pack()
input_label = tk.Label(window, text="Enter Text:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()
translate_button = tk.Button(window, text="Translate", command=translate)
translate_button.pack()
window.mainloop()