#!/usr/bin/env python3

# Diogo Mateiro     nº  97812
# Gonçalo Ornelas   nº  105037
# Gustavo Reggio    nº  118485 

from pprint import pprint
from colorama import Fore, Back, Style
from time import time, ctime
import readchar as r
import argparse
import string
import random
from random_word import RandomWords
from collections import namedtuple

def use_words_characters(use_words,max_value,use_time_mode): #words or single character defined as a function

    """Function which define the main imputs for defining the game mode.

    Args: 
            use_words       : returns strings with values words/chars.

            max_value       : returns the amunto of time or inputs of the game.
            
            use_time_mode   : returns the mode.

    Value:
    
    """

    Input = namedtuple('Input', ['requested', 'received','duration']) #Tuple with 3 parameters
    lst = []
    i = 0                       #simple counter just to avoid using len functions and such
    l = 0                       #for accuracy purposes
    dt_begin = ctime()          #formates time and date
    miss_time = 0               #for later parameters
    hit_time = 0                #for later parameters (dictionary related)
    
    if use_words == "char":     #In case it was defined the letter program
        z = time()              #start time

        while True:
            k = time()          #used not for total time, but for time between seeing the letter and typing it
            y = random.choice(string.ascii_lowercase) #defines a random lower case letter as a string
            print('Type letter ' + y )
            
            x = r.readkey()
            j = time()                  #endtime
            
            if x != r.key.SPACE:        #To not save any parameters in case of space
                if x == y: 
                    print(Fore.GREEN+'You pressed the right key!'+Style.RESET_ALL) #User interface just to tell the dude he did right or not
                    l += 1              #Using this to calculate accuracy, since its faster to use a simple counter than to compare every argument
                    hit_time += (j-k)   #it will accumulate the time it took to hit
                    print('You typed: '+Fore.GREEN + x + Style.RESET_ALL + ' In:' + str("%.2f" %(j-k)) + ' secs')

                else:
                    print(Fore.RED + 'You pressed the wrong key!' + Style.RESET_ALL)
                    miss_time += (j-k)  #it will accumulate the time it took to miss
                    print('You typed: '+Fore.RED + x + Style.RESET_ALL + ' In:' + str("%.2f" %(j-k)) + ' secs')
                
                n = Input(y,x, float("%.2f" %(j-k)))    #creates a named tuple with predefined parameters
                lst.append(n)           #appends the named tuple into an empty list
            
            #print('You typed '+x)      #After being told he pressed right or wrong, prints what was typed

            elapsed_time = (j-z)        #Elapsed time between when it started and when it ended
            i += 1
            
            if use_time_mode == "time": #If timemode was the option
                if (elapsed_time >= max_value or x == r.key.SPACE):

                    dt_end = ctime()    #dt format

                    dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time)
                    break
                
            elif use_time_mode == "input": #if inputmode was the option
                if i == max_value or x == r.key.SPACE:
                
                    dt_end = ctime()       #dt format

                    dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time)
                    break

    elif use_words == "word":           #In case its defined as complete words

        z = time()                      #start time
        
        w = ""                          #just for the word its being written

        while True:
            o = RandomWords()           #generates random words
            y = o.get_random_word()     #gets the random word
            print('Type word: \n'+ y)
            k = time()                  #local time per word
            

            while True:
                
                x = r.readkey()
                w += x                         #key is read and saved
                print(x,end="", flush=True)    #Permits showing the typing of the word

                if x != r.key.SPACE:           #In case of space
                    if len(w) == len(y):       #stops
                        j = time()             #stops the time it was type
                        if w == y: 

                            print(Fore.GREEN+'\nYou wrote the right word!'+ Style.RESET_ALL) #User interface just to tell the dude he did right or not
                            l += 1              #Using this to calculate accuracy, since its faster to use a simple counter than to compare every argument
                            hit_time += (j-k)   #it will accumulate the time it took to hit
                            print('You typed: '+Fore.GREEN + w + Style.RESET_ALL + ' In:' + str("%.2f" %(j-k)) + ' secs\n')

                        else:
                            print(Fore.RED+'\nYou wrote the wrong word!'+Style.RESET_ALL)                            
                            miss_time += (j-k)  #it will accumulate the time it took to miss
                            print('You typed: '+Fore.RED + w + Style.RESET_ALL + ' In:' + str("%.2f" %(j-k)) + ' secs\n')

                        n = Input(y,w,float("%.2f" %(j-k)))    #creates a named tuple with predefined parameters
                        lst.append(n)           #appends the named tuple into an empty list

                        #print('You typed '+w) #After being told he pressed right or wrong, prints what was typed
                        
                        i += 1
                        
                        w = ""

                        break

                else: break                     #Doesnt save anything in case of space
            
            elapsed_time = (j-z)                #Elapsed time between when it started and when it ended
               
            if use_time_mode == "time":         #If timemode was the option
                if (elapsed_time >= max_value or x == r.key.SPACE):
                    dt_end = ctime()            #dt format
        
                    dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time)
                    break
                
            elif use_time_mode == "input":      #if inputmode was the option
                if i == max_value or x == r.key.SPACE:
                    dt_end = ctime()            #dt format
        
                    dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time)
                    break  
    else: print('Parameters defined incorrectly')  #just in case someone makes a mistake defining parameters          

def dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time):

    """ This function is only for listing  the statistics of the game.

    Args: 
          l             : Total number of correct answers
          i             : Total numbers of answers given
          lst           : The list which contains: requested word/char, received input, duration of the input
          elapsed_time  : Game time
          dt_end        : Indicational time of the end of the game
          dt_begin      : Indicational time of the beginning of the game
          hit_time      : The time that the user took to answered correctly
          miss_time     : The time that the user took to answered wrongly
    
    """


    d={}
    
    d['accuracy']=(l/i)                         #accuracy is defined by number of hits divided by the total number of chances
    d['inputs']=lst                             # Namedtuple of the requested word/char, received input, duration of the input
    d['number_of_hits']=l                        
    d['number_of_types']=i
    d['test_duration']="%.2f" %elapsed_time
    
    d['test_end']=dt_end
    d['test_start']=dt_begin
    
    q=0
    for p in range(0,len(lst)):                 #used in order to calculate average duration
        q += lst[p].duration
    
    d["type_average_duration"]="%.2f" %(q/i)
    d["type_hit_average_duration"]="%.2f" %(hit_time/i)
    d["type_miss_average_duration"]="%.2f" %(miss_time/i)
    
    pprint(d)
    

def main():
    """ Main Function defines the arguments which the user will be requested and it cals the use_words_characters function.

    Args    : NONE

    Value   : NONE
    
    """
    
    #Process command line and arguments
    parser = argparse.ArgumentParser(description = "Scrip used to test your typing")
    parser.add_argument("-utm",'--use_time_mode', type=str, choices = ["time","input"], help ='Uses ' + Fore.RED + 'time mode ' + Fore.RESET + 'or ' + Fore.RED + 'input mode' + Fore.RESET, required = True)
    parser.add_argument("-mv",'--max_value', type=int, help ='Max numbers of secs for ' + Fore.RED + 'time mode ' + Fore.RESET +'or maximum number of inputs for number of inputs mode ', required = True)
    parser.add_argument("-uw",'--use_words', type=str, choices = ["word","char"] ,help = 'Use word typing or single character mode', required = False, default= "char")
    
    args = vars(parser.parse_args())            #creates a dictionary


    if (args['use_time_mode'] == 'time'):

        # Tells the configuration of the game
        print("Starting game of typing test \nMode: " + args['use_words'] + ' e ' + args['use_time_mode'] +
            "\nDuration: " + str(args['max_value']) + " seconds\n")
        
    else:
        # Tells the configuration of the game
        print("Starting game of typing test \nMode: " + args['use_words'] + ' e ' + args['use_time_mode'] + 
        "\nNumber of inputs: " + str(args["max_value"])+ "\n")


    print('Press any key to start')

    while True:                               #simple cycle to start the program after key was pressed
        m = r.readkey() 

        if m != "": 
            print('Your typing test will start now\n')
            break
  

    use_words_characters(args["use_words"],args["max_value"],args["use_time_mode"])               



if __name__ == "__main__":
    main()