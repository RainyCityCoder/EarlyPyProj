# MorseTranslator
Various programs that translate English into Morse Code and visa versa. 

README file for RainyCityDiver's Morse Code Translator

DESCRIPTION:
This program is designed to translate letters and/or numbers into morse code, and visa versa. 
Built on Python 3.6.9.

INSTALLATION:
Download the .py file of your choice from the https://github.com/RainyCityDiver/MorseTranslator repository, or copy-paste the code into a Python file of your own. Please see the license file.

TO START:
1) Open file with your choice of Python-3-capable IDE, or run in a terminal capable of running Python 3 files. 
2) Run the program.
3.1) For MorseCodeTranslator.py and MCTranslator.py, the program will first ask for one of two options:
    a) Morse-to-Letter translation.
    b) Letter-to-Morse translation.
4.1) Select which you wish to use by entering the corresponding letter.

3.2) For MCTranstkinter.py, a window will appear. 

FOR MORSE-TO-LETTERS:
Please Note: The input only accepts hyphens ("-") as dashes, and periods (".") as dots at this time. 
Please Note: Spaces, numbers, and punctuation are allowed.
1.1) After selecting Morse-to-Letter, type or copy-paste the string of morse code you wish to convert to English when prompted.
2.1) It is best to separate each letter with a space. Morse letters are between 2 and 4 dots and/or dashes long. 
  a) If you enter '--.-', the program will return 'q'. If you meant to type '--' '.-', for 'm a' the program can't tell which you intended, unless spaces are used properly.

1.2) Once the window appears you may enter English characters or Morse Code into the upper text entry field, and select your choice of two buttons:
    a)"Morse-to-English" button will translate Morse Code into English characters
    b)"English-to-Morse" button will translate English characters into Morse Code
  
FOR LETTERS-TO-MORSE:
Please Note: Spaces, numbers, and punctuation are allowed.
1) After selecting Letter-to-Morse, type your letters/words/numbers/etc. 
  a) Spaces will not be inserted between letters (see ROADMAP).
  b) You may type with spaces between words OR between each letter, depending on your desired output.README file for RainyCityDiver's Morse Code Translator

OUTPUT:
Program returns one of these results, depending on the file used: 
MCTranslator.py: a list containing characters (in string format) of the translation of input characters in the Python interpreter
MCTranstkinter: string consisting of characters of the translation of input characters in the lower text field
MorseCodeTranslator.py: string consisting of characters of the translation of input characters in the Python interpreter

RE-RUN:
For MCTranslator.py and MorseCodeTranslator.py, you will be asked if you would like to translate again; simply enter "y" for yes, or "n" for no. 
NOTE: You will need to select Morse-to-Letter translation or Letter-to-Morse translation again. This prevents the user from needing to re-run the entire program to switch between the two modes. This is a feature, not a bug (no, seriously).
For MCTranstkinter.py, to translate additional strings of Morse Code or English, delete the initial input text/Morse Code from the upper text entry field, and press the corresponding translate button.
  
SUPPORT:
You may reach out to the creator via GitHub with suggestions to improve program (see ROADMAP).

ROADMAP/FUTURE FUNCTIONALITY:
1) Multiple-run functionality is being explored for future implementation. -DONE
2) In Letter-to-Morse mode: Spaces inserted between Morse letters in MorseCodeTranslator.py. 
3) In Letter-to-Morse mode: Character indicating seperation between words for easier reading in MorseCodeTranslator.py. 
4) In Morse-to-Letter mode: spaces between letter groups in MorseCodeTranslator.py. 
5) Support for Arabic numerals. -DONE
6) GUI version. -ALMOST DONE

CONTRIBUTIONS:
Contributions are welcome, preferably as messages to the creator containing suggestions to enhance functionality/fix bugs, with template code attached so the creator can problem-solve or implement new code on their own. The creator is currently building experience with Python 3, and with coding in general. Allowing the creator to learn and develope their skills is of more value to them than providing functional code and saying "put this in line X". Thank you for your understanding.

PROJECT STATUS
The Morse Code Translator is under developement. 

CHANGELOG:
2021.03.02: added support for repeated translations without needing to re-run program, and support for arabic numbers. 
2021.10.13: Added version that outputs to list, hopefully making future integration with website/web app easier.
2021.11.30: Added GUI version based on tkinter. 



This document is not final and is subject to modification. 
