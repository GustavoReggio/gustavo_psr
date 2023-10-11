#!/usr/bin/env python3
#First pratical work 
from colorama import Fore, Back, Style
import time
import readchar as r
import argparse
import string
import random
from random_word import RandomWords
from collections import namedtuple

def use_words_characters(use_words,max_value,use_time_mode): #words or single character defined as a function
    Input = namedtuple('Input', ['requested', 'received','duration']) #Tuple with 3 parameters
    lst=[]
    i=0 #simple counter just to avoid using len functions and such
    l=0 #for accuracy purposes
    begin=time.localtime() #saves starting time and date
    dt_begin= time.strftime("%a %b %d %H:%M:%S %Y",begin) #formates time and date
    miss_time=0 #for later parameters
    hit_time=0  #for later parameters (dictionary related)
    
    if use_words=="singlechar": #In case it was defined the letter program
        z=time.time() #start time

        while True:
            k=time.time() #used not for total time, but for time between seeing the letter and typing it
            y=random.choice(string.ascii_lowercase) #defines a random lower case letter as a string
            print('Type letter '+y )
            
            x=r.readkey()
            j=time.time() #endtime
            
            if x!=r.key.SPACE:#To not save any parameters in case of space
                if x==y: 
                    print(Fore.GREEN+'You pressed the right key!'+Style.RESET_ALL) #User interface just to tell the dude he did right or not
                    l+=1 #Using this to calculate accuracy, since its faster to use a simple counter than to compare every argument
                    hit_time+=(j-k) #it will accumulate the time it took to hit
                else:
                    print(Fore.RED+'You pressed the wrong key!'+Style.RESET_ALL)
                    miss_time+=(j-k) #it will accumulate the time it took to miss
                
                n=Input(y,x,(j-k)) #creates a named tuple with predefined parameters
                lst.append(n) #appends the named tuple into an empty list
            
            #print('You typed '+x) #After being told he pressed right or wrong, prints what was typed

            elapsed_time=(j-z) #Elapsed time between when it started and when it ended
            i+=1
            
            if use_time_mode=="time": #If timemode was the option
                if (elapsed_time>=max_value or x==r.key.SPACE):

                    end=time.localtime() #saves current time and date
                    dt_end= time.strftime("%a %b %d %H:%M:%S %Y",end) #dt format
        
                    dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time)
                    break
                
            elif use_time_mode=="input": #if inputmode was the option
                if i==max_value or x==r.key.SPACE:
                    
                    end=time.localtime() #saves current time and date
                    dt_end= time.strftime("%a %b %d %H:%M:%S %Y",end) #dt format
        
                    dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time)
                    break

    elif use_words=="word": #In case its defined as complete words
        z=time.time() #start time
        
        w="" #just for the word its being written
        while True:
            o=RandomWords() #generates random words
            y=o.get_random_word() #gets the random word
            print('Type word '+y)
            
            while True:
                k=time.time() #local time per word
                
                x=r.readkey()
                w+=x #key is read and saved
                
                if x!=r.key.SPACE: #In case of space
                    if len(w)==len(y): #stops
                        j=time.time() #stops the time it was type
                        if w==y: 
                            print(Fore.GREEN+'You wrote the right word!'+Style.RESET_ALL) #User interface just to tell the dude he did right or not
                            l+=1 #Using this to calculate accuracy, since its faster to use a simple counter than to compare every argument
                            hit_time+=(j-k) #it will accumulate the time it took to hit
                        else:
                            print(Fore.RED+'You wrote the wrong word!'+Style.RESET_ALL)                            
                            miss_time+=(j-k) #it will accumulate the time it took to miss

                        n=Input(y,w,(j-k)) #creates a named tuple with predefined parameters
                        lst.append(n) #appends the named tuple into an empty list
                        #print('You typed '+w) #After being told he pressed right or wrong, prints what was typed
                        
                        i+=1
                        
                        w=""
                        break
                else: break #Doesnt save anything in case of space
            
            elapsed_time=(j-z) #Elapsed time between when it started and when it ended
               
            if use_time_mode=="time": #If timemode was the option
                if (elapsed_time>=max_value or x==r.key.SPACE):

                    end=time.localtime() #saves current time and date
                    dt_end= time.strftime("%a %b %d %H:%M:%S %Y",end) #dt format
        
                    dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time)
                    break
                
            elif use_time_mode=="input": #if inputmode was the option
                if i==max_value or x==r.key.SPACE:
                    
                    end=time.localtime() #saves current time and date
                    dt_end= time.strftime("%a %b %d %H:%M:%S %Y",end) #dt format
        
                    dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time)
                    break  
    else: print('Parameters defined incorrectly')  #just in case someone makes a mistake defining parameters          

def dictionary(l,i,lst,elapsed_time,dt_end,dt_begin,hit_time,miss_time):
    d={}
    
    d['accuracy']=(l/i) #accuracy is defined by number of hits divided by the total number of chances
    d['inputs']=lst
    d['number_of_hits']=l
    d['number_of_types']=i
    d['test_duration']=elapsed_time
    
    d['test_end']=dt_end
    d['test_start']=dt_begin
    
    q=0
    for p in range(0,len(lst)): #used in order to calculate average duration
        q+=lst[p].duration
    
    d["type_average_duration"]=q/elapsed_time
    d["type_hit_average_duration"]=hit_time/elapsed_time
    d["type_miss_average_duration"]=miss_time/elapsed_time
    
    print(d)
    

def main():
    
    #Process command line and arguments
    parser = argparse.ArgumentParser(description="Scrip used to test your typing")
    parser.add_argument("-utm",'--use_time_mode',type=str,choices=["time","input"],help='Uses time mode or input mode',required=True)
    parser.add_argument("-mv",'--max_value',type=int, help='Max numbers of secs for time mode or maximum number of inputs for number of inputs mode',required=True)
    parser.add_argument("-uw",'--use_words',type=str,choices=["word","singlechar"] ,help='Use word typing or single character mode',required=True)
    
    args=vars(parser.parse_args()) #creates a dictionary
    
    print('Press any key to start')
    while True: #simple cycle to start the program after key was pressed
        m=r.readkey() 
        if m!="": 
            print('Your typing test will start now')
            break
  

    use_words_characters(args["use_words"],args["max_value"],args["use_time_mode"])               



if __name__ == "__main__":
    main()