#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Characters and corresponding Morse.
# Unsure how I want to handle single-space; I might need a way to white-space
# between words in Morse Code output. Leaving as (' ','-.-.-.-') for now.
giant_list = [
    ('a','.-'), ('b','-...'), ('c','-.-.'), ('d','-..'),
    ('e','.'), ('f','..-.'), ('g','--.'), ('h','....'),
    ('i','..'), ('j','.---'), ('k','-.-'), ('l','.-..'),
    ('m','--'), ('n','-.'), ('o','---'), ('p','.--.'),
    ('q','--.-'), ('r','.-.'), ('s','...'), ('t','-'),
    ('u','..-'), ('v','...-'), ('w','.--'), ('x','-..-'),
    ('y','-.--'), ('z','--..'), 
    (' ','-.-.-.-'), 
    ('1','.----'), ('2','..---'), ('3','...--'), ('4','....-'),
    ('5','.....'), ('6','-....'), ('7','--...'), ('8','---..'), 
    ('9','----.'), ('0','-----'), 
    ('.','.-.-.-'), (',','--..--'), ('?','..--..'), ("'",".----."), 
    ('!','-.-.--'), ('/','-..-.'), ('(','-.--.'), (')','-.--.-'), 
    ('&','.-...'), (':','---...'), (';','-.-.-.'), ('=','-...-'), 
    ('+','.-.-.'), ('-','-....-'), ('_','..--.-'), ('"','.-..-.'), 
    ('$','...-..-'), ('@','.--.-.'),
    ('<End of Work>','...-.-'), ('<Error>','........'), ('<Start>','-.-.-') 
    ]

# Build dictionary with character as key (thanks raeq on Discord)
e_to_m: dict = {i[0]: i[1] for i in giant_list}
# Could also use e_to_m = dict(giant_list)

# Build dictionary with morse code as key (thanks raeq on Discord)
m_to_e: dict = {i[1]: i[0] for i in giant_list}
# Could also use m_to_e = dict(map(reversed, giant_list))

# Leaving these two as dict comprehension because it was good practice

def from_letters(code_input) -> list :
    """Translate letters to Morse"""
    # output = ""
    characters = code_input.lower()
    for letter in characters:
        return [e_to_m.get(letter, '?') for letter in characters]
    

def from_morse(code_input) -> list :
    """Convert Morse to letters"""
    # output = ""
    # code = code_input.split(' ') 
    for letter in code_input:
        return [m_to_e.get(letter, '?') for letter in code_input]
       

restart = "y"

while restart != "n":
# Ask user for desired direction of translation
    print("""Please select the following:
M for Morse-to-Letters, or 
L for Letters-to-Morse""")
    morse_original = input("> ")
    morse = morse_original.lower()

# If user selects morse-to-english: use from_letters to convert to Morse
    if morse == 'l':
        code_input = input("""Please write/paste characters here
(spaces between words): """)
        print("Here it is in Morse Code:", from_letters(code_input))
        restart_input = input("Another? (y/n) ")
        restart = restart_input.lower()

# If user selects english-to-morse: use from_morse to convert to English
    elif morse == 'm':
        code_input = input("""Please write/paste string here:
(periods for dots and hyphens for dashes and *spaces
between letters*): """)
        print("Here it is in characters:", from_morse(code_input))
        restart_input = input("Another? (y/n) ")
        restart = restart_input.lower()

# If user doesn't input "M" or "L", ask if they want another go
    else:
        restart_input = input("Another? (y/n) ")
        restart = restart_input.lower()

