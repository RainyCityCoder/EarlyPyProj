#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

# Close window function
def close_window():
    window.destroy()
    exit()

# Translation functions:    
def from_letters(code_input):
    """Translate letters to Morse"""
    entered_text=textentry.get() #Gets text from text entry box
    output.delete(0.0, END) #Deletes prior output text
    try:
        translation = e_to_m[entered_text]
    except:
        translation = "Something's wrong. Please check entry and try again."
    output.insert(END, translation)
    

def from_morse(code_input):
    """Convert Morse to letters"""
    entered_text=textentry.get() #Gets text from text entry box
    output.delete(0.0, END) #Deletes prior output text
    try:
        translation = m_to_e[entered_text]
    except:
        translation = "Something's wrong. Please check entry and try again."
    output.insert(END, translation)
    

# Window
window = Tk()
window.title("Morse Code Translator")
window.configure(background="black")

# Entry field label
Label (window, text="Please enter Morse/Text, and choose one option:", 
       bg="black", fg="white", font="none 12 bold") .grid(row=0, column=0, 
                                                          sticky=W)

# Text entry field
textentry = Entry(window, width=40, bg="white")
textentry.grid(row=1, column=0, sticky=W)

# Buttons to trigger translation (outputs to output field)
Button(window, text="Morse-to-English", width=0, command=from_morse) .grid(row=2,
                                                                  column=0,
                                                                  sticky=W)
Button(window, text="English-to-Morse", width=0, command=from_letters) .grid(row=2,
                                                                  column=1,
                                                                  sticky=W)
# Output field label
Label (window, text="\nTranslation:", bg="black", fg="white", 
       font="none 12 bold") .grid(row=3, column=0, sticky=W)

# Output field
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=4, column=0, stick=W)

# Dictionaries
# English letters and corresponding Morse
e_to_m = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
    'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
    'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
    'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
    'y':'-.--', 'z':'--..', ' ':'-.-.-.-', '1':'.----',
    '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...',
    '8':'---..', '9':'----.', '0':'-----',
    '.':'.-.-.-', ',':'--..--', '?':'..--..',
    "'":".----.", '!':'-.-.--', '/':'-..-.',
    '(':'-.--.', ')':'-.--.-', '&':'.-...',
    ':':'---...', ';':'-.-.-.', '=':'-...-',
    '+':'.-.-.', '-':'-....-', '_':'..--.-',
    '"':'.-..-.', '$':'...-..-', '@':'.--.-.',
    '<End of Work>':'...-.-', '<Error>':'........',
    '<Start>':'-.-.-' 
    } 

# Morse code and corresponding English letters
m_to_e = {
    '.-':'a', '-...':'b', '-.-.':'c', '-..':'d',
    '.':'e', '..-.':'f', '--.':'g', '....':'h',
    '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
    '--':'m', '-.':'n', '---':'o', '.--.':'p',
    '--.-':'q', '.-.':'r', '...':'s', '-':'t',
    '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
    '-.--':'y', '--..':'z', '-.-.-.-':' ', '.----':'1',
    '..---':'2', '...--':'3', '....-':'4',
    '.....':'5', '-....':'6', '--...':'7',
    '---..':'8', '----.':'9', '-----':'0',
    '.-.-.-':'.', '--..--':',', '..--..':'?',
    ".----.":"'", '-.-.--':'!', '-..-.':'/',
    '-.--.':'(', '-.--.-':')', '.-...':'&',
    '---...':':', '-.-.-.':';', '-...-':'=',
    '.-.-.':'+', '-....-':'-', '..--.-':'_',
    '.-..-.':'"', '...-..-':'$', '.--.-.':'@',
    '...-.-':'<End of Work>', '........':'<Error>',
    '-.-.-':'<Start>'
    } 

# Exit button
Button(window, text="Exit", width=0, command=close_window) .grid(row=5,
                                                                  column=0,
                                                                  sticky=W)

# Run main loop
window.mainloop()
       

# Probably don't need in this version of the program
# restart = "y"

# while restart != "n":
# # Ask user for desired direction of translation
#     print("""Please select the following:
# M for Morse-to-Letters, or 
# L for Letters-to-Morse""")
#     morse_original = input("> ")
#     morse = morse_original.lower()

# # If user selects morse-to-english: use from_letters to convert to Morse
#     if morse == 'l':
#         code_input = input("""Please write/paste characters here
# (spaces between words): """)
#         print("Here it is in Morse Code:", from_letters(code_input))
#         restart_input = input("Another? (y/n) ")
#         restart = restart_input.lower()

# # If user selects english-to-morse: use from_morse to convert to English
#     elif morse == 'm':
#         code_input = input("""Please write/paste string here:
# (periods for dots and hyphens for dashes and *spaces
# between letters*): """)
#         print("Here it is in characters:", from_morse(code_input))
#         restart_input = input("Another? (y/n) ")
#         restart = restart_input.lower()

# # If user doesn't input "M" or "L", ask if they want another go
#     else:
#         restart_input = input("Another? (y/n) ")
#         restart = restart_input.lower()

