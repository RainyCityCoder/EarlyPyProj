e_to_m = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
    'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
    'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
    'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
    'y':'-.--', 'z':'--..', ' ':' ', '1':'.----',
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
# English letters and corresponding Morse

m_to_e = {
    '.-':'a', '-...':'b', '-.-.':'c', '-..':'d',
    '.':'e', '..-.':'f', '--.':'g', '....':'h',
    '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
    '--':'m', '-.':'n', '---':'o', '.--.':'p',
    '--.-':'q', '.-.':'r', '...':'s', '-':'t',
    '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
    '-.--':'y', '--..':'z', ' ':' ', '.----':'1',
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
# Morse code and corresponding English letters

restart = "y"

def from_letters(code_input):
    """Translate letters to Morse"""
    output = ""
    code = code_input.lower()
    for letter in code:
        output += e_to_m.get(letter, '?')
    return output
    

def from_morse(code_input):
    """Convert Morse to letters"""
    output = ""
    code = code_input.split(' ') 
    for letter in code:
        output += m_to_e.get(letter, '?')
    return output
       

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

