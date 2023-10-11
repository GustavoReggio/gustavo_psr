#Teste 2

import curses
import time
import random
from curses import wrapper


def start_screen(stdscr):
    
    stdscr.clear()
    stdscr.addstr("Speed Typing Test")  

                                        #O método addstr() recebe uma string Python ou bytestring como o valor a ser apresentado.
                                        #O conteúdo de bytestrings é enviado para o terminal tal como está. 
                                        #As cadeias de caracteres são codificadas para bytes usando o valor do atributo de codificação da janela;
                                        #a predefinição é a codificação predefinida do sistema como devolvida pelo método local

    stdscr.addstr("\n Press any key to start: ")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0): #wpm = word per minut
    
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(i)
        
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0,i,char,color)

def load_text():

    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):

    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text)/(time_elapsed/60))/5)
    
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
                                            #The ord() function returns the number representing the unicode code of a specified character.
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
                                            #Dentro de um intervalo de caracteres, \b representa o carácter backspace, 
                                            # para compatibilidade com os literais de cadeia de caracteres do Python.
                                            #An Ancient Character Set :Values are between 0–127 (x00–x7F)
            if len(current_text) > 0:
                current_text.pop()

            elif len(current_text) < len(target_text):
                current_text.append(key)
    
def main (stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0, "You have completed the test! Press anything to continue: ")
        key = stdscr.getch()

        if ord(key) == 27:
            break

wrapper(main)

