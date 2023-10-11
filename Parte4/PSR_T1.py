#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python


#First pratical work

#All the imports that will be used on the program
import time
from colorama import Fore, Back, Style
#from time import time, ctime
from pprint import pprint
import readchar as r
import argparse
import string
import random
from random_word import RandomWords
from collections import namedtuple



def main():
    """
    
    """
    
    #Process command line and arguments
    parser = argparse.ArgumentParser(description="Scrip used to test your typing")
    parser.add_argument("-utm",'--use_time_mode',type=str, help='Uses time mode if True and input mode if False',required=True)
    parser.add_argument("-mv",'--max_value',type=int, help='Max numbers of secs for time mode or maximum number of inputs for number of inputs mode',required=True)
    parser.add_argument("-uw",'--use_words',type=str, help='Use word typing mode if TRUE, instead of single character typing (FALSE)',required=True)
    
    args=vars(parser.parse_args())      #creates a dictionary
    
    print('Press any key to start')
    while True:                         #simple cycle to start the program after key was pressed
        confir_input = r.readkey()      #Waiting for the confirmation of the user
        if confir_input != "":          #Ensure the user typed something to start the game
            print('Your typing test will start now')
            break
  

    Input_mode = namedtuple('Input', ['requested', 'received','duration']) #Tuple with 3 parameters
    lst = []                            #Empty list as yeasy variable
    counter_elaps = 0                               #simple counter just to avoid using len functions and such
    l = 0                               #for accuracy purposes
    begin = time.localtime()            #saves starting time and date
    init_game_time = time.strftime("%a %b %d %H:%M:%S %Y",begin) #formates time and date
    miss_time = 0                       #for later parameters
    hit_time = 0                        #for later parameters (dictionary related)
    
    
    if args["use_words"] == "False":    #In case it was defined the letter program
        time_start = time.time()        #start time

        while True:
            typing_time = time.time()                 #used not for total time, but for time between seeing the letter and typing it
            word_random = random.choice(string.ascii_lowercase) #defines a random lower case letter as a string
            print('Type letter '+word_random )
            
            x = r.readkey()
            j = time.time()             #endtime
            
            if x != r.key.SPACE:        #To not save any parameters in case of space
                if x == word_random: 
                    print(Fore.GREEN+'You pressed the right key!'+Style.RESET_ALL) #User interface just to tell the dude he did right or not
                    l += 1              #Using this to calculate accuracy, since its faster to use a simple counter than to compare every argument
                    hit_time += (j-typing_time)   #it will accumulate the time it took to hit
                else:
                    print(Fore.RED+'You pressed the wrong key!'+Style.RESET_ALL)
                    miss_time += (j-typing_time) #it will accumulate the time it took to miss
                
                n=Input_mode(word_random,x,(j-typing_time)) #creates a named tuple with predefined parameters
                lst.append(n)           #appends the named tuple into an empty list
            
            #print('You typed '+x) #After being told he pressed right or wrong, prints what was typed

            elapsed_time=(j-time_start) #Elapsed time between when it started and when it ended
            counter_elaps+=1
            
            if args['use_time_mode']=="True": #If timemode was the option
                if (elapsed_time>=args["max_value"] or x==r.key.SPACE):

                    end=time.localtime() #saves current time and date
                    dt_end= time.strftime("%a %b %d %H:%M:%S %Y",end) #dt format
        
                    dictionary(l,counter_elaps,lst,elapsed_time,end,dt_end,init_game_time,hit_time,miss_time)
                    break
                
            else: #if inputmode was the option
                if counter_elaps==args["max_value"] or x==r.key.SPACE:
                    
                    end=time.localtime() #saves current time and date
                    dt_end= time.strftime("%a %b %d %H:%M:%S %Y",end) #dt format
        
                    dictionary(l,counter_elaps,lst,elapsed_time,end,dt_end,init_game_time,hit_time,miss_time)
                    break

    elif args["use_words"]=="True": #In case its defined as complete words
        time_start=time.time() #start time
        
        w="" #just for the word its being written
        while True:
            o=RandomWords() #generates random words
            word_random=o.get_random_word() #gets the random word
            print('Type word '+word_random)
            
            while True:
                typing_time=time.time() #local time per word
                
                x=r.readkey()
                w+=x #key is read and saved
                
                if x!=r.key.SPACE: #In case of space
                    if len(w)==len(word_random): #stops
                        j=time.time() #stops the time it was type
                        if w==word_random: 
                            print(Fore.GREEN+'You wrote the right word!'+Style.RESET_ALL) #User interface just to tell the dude he did right or not
                            l+=1 #Using this to calculate accuracy, since its faster to use a simple counter than to compare every argument
                            hit_time+=(j-typing_time) #it will accumulate the time it took to hit
                        else:
                            print(Fore.RED+'You wrote the wrong word!'+Style.RESET_ALL)                            
                            miss_time+=(j-typing_time) #it will accumulate the time it took to miss

                        n=Input_mode(word_random,w,(j-typing_time)) #creates a named tuple with predefined parameters
                        lst.append(n) #appends the named tuple into an empty list
                        #print('You typed '+w) #After being told he pressed right or wrong, prints what was typed
                        
                        counter_elaps+=1
                        
                        w=""
                        break
                else: break #Doesnt save anything in case of space
            
            elapsed_time=(j-time_start) #Elapsed time between when it started and when it ended
               
            if args['use_time_mode']=="True": #If timemode was the option
                if (elapsed_time>=args["max_value"] or x==r.key.SPACE):

                    end=time.localtime() #saves current time and date
                    dt_end= time.strftime("%a %b %d %H:%M:%S %Y",end) #dt format
        
                    dictionary(l,counter_elaps,lst,elapsed_time,end,dt_end,init_game_time,hit_time,miss_time)
                    break
                
            else: #if inputmode was the option
                if counter_elaps==args["max_value"] or x==r.key.SPACE:
                    
                    end=time.localtime() #saves current time and date
                    dt_end= time.strftime("%a %b %d %H:%M:%S %Y",end) #dt format
        
                    dictionary(l,counter_elaps,lst,elapsed_time,end,dt_end,init_game_time,hit_time,miss_time)
                    break  
    else: print('Parameters defined incorrectly')  #just in case someone makes a mistake defining parameters          
                


def dictionary(l,i,lst,elapsed_time,end,end_time,start_time,hit_time,miss_time):

    """This functiion is only to store the final results of the game.


    Args:

        l:
        i:
        lst:
        elapsed_time:
        end,dt_end,dt_begin:
        hit_time:
        miss_time:


    Value:

    """
    d={}
    
    d['accuracy']=(l/i) #accuracy is defined by number of hits divided by the total number of chances
    d['inputs']=lst
    d['number_of_hits']=l
    d['number_of_types']=i
    d['test_duration']=elapsed_time
    
    d['test_end']=end_time
    d['test_start']=start_time
    
    q=0
    for p in range(0,len(lst)): #used in order to calculate average duration
        q+=lst[p].duration
    
    d["type_average_duration"]=q/elapsed_time
    d["type_hit_average_duration"]=hit_time/elapsed_time
    d["type_miss_average_duration"]=miss_time/elapsed_time
    
    pprint(d)
    

if __name__ == "__main__":
    main()