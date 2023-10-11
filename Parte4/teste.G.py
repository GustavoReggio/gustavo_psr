#!/usr/bin/env python3

import random
import argparse
from pprint import pprint
from collections import namedtuple
from time import time, ctime
from colorama import Back, Fore, Style
from readchar import readkey  
from random_word import RandomWords

# The list which contains the characters/Word + the input + the time required for the input
list_inputs = []

end_time = 0
count = 0
count_right = 0
count_wrong = 0
cumTime = 0
cumTimeRight = 0
cumTimeWrong = 0
init_game_time = ctime()
end_game_time = 0


Input = namedtuple('Input', ['requested', 'received', 'duration'])

# 
def arguments():

    """This function define the arguments that the user will need to type when call the program.
       The user need to type: ./name_of_the_file.py -utm [time/inputs] -mv [number of the time or inputs] -uw [ /words]

        Args:

        Value:
    """

    # Define variable to process commands

    parser = argparse.ArgumentParser(description = 'Menu of typing game')
    
    # Add argument to choose max time to evaluate 
    # Add argument to choose the mode 
    parser.add_argument('-utm', '--use_time_mode', 
                        type=str, 
                        choices=['time', 'inputs'], 
                        help='Decide the type of challenge ' + Fore.RED + 'Time Mode ' + Fore.RESET + 'or ' + 
                        Fore.RED + 'Inputs Mode' + Fore.RESET, 
                        required=True)
    
    # Add argument to choose max number of inputs 
    parser.add_argument('-mv', '--MAX_VALUE', 
                        type=int, 
                        help='Max number of seconds ' + Fore.RED + 'for time ' + Fore.RESET + 'or maximum number of inputs ' +
                         Fore.RED + 'for inputs' + Fore.RESET, 
                        required=True)
    
    # Add argument to choose the type of typing game
        # Argument does not require choice: characters. It set to be empty 
    parser.add_argument('-uw', '--uses_words', 
                        type=str, 
                        choices=['characters', 'words'], 
                        help='Use word typing mode, instead of single character typing', 
                        required=False,
                        default='characters')

    # Create a dictionary
    args = vars(parser.parse_args())

    if (args['use_time_mode'] == 'time'):

        # Tells the configuration of the game
        print("Starting game of typing test \nMode: " + args['uses_words'] + ' e ' + args['use_time_mode'] +
            "\nDuration: " + str(args['MAX_VALUE']) + " seconds")
        
    else:
        # Tells the configuration of the game
        print("Starting game of typing test \nMode: " + args['uses_words'] + ' e ' + args['use_time_mode'] + 
        "\nNumber of inputs: " + str(args["MAX_VALUE"]))

    print("Press any key to start the typing test...")

    wait_key = readkey()

    # choosing the game mode
    if(args['uses_words'] == 'characters'):
        mod_char(args['MAX_VALUE'], args['use_time_mode'])

    else:
        mod_word(args['MAX_VALUE'], args['use_time_mode']) 


# Characters Functoin  
def mod_char(num_inputs, mode):

    """This function is only for Character Mode. 

    Args:
        num_inputs: value set on MAX_VALUE (in arguments funcion)

        mode: value set on use_time_mode (in arguments funcion)

    Value:

    
    """

    
    #end_time = 0
    #count = 0
    #count_right = 0
    #count_wrong = 0
    #cumTime = 0
    #cumTimeRight = 0
    #cumTimeWrong = 0
    #init_game_time = ctime()
    #end_game_time = 0
    
    #Input Mode for Characters
    if mode == 'inputs':
        init_time = time()

        while True:
            random_char = random.randint(97, 122)
            init_char_time = time()
            print(chr(random_char))
            input_key = readkey()

            if (input_key == ' '):
                break

            elif input_key == chr(random_char):
                end_char_time = time() - init_char_time
                print(input_key + Fore.GREEN + " Correct key " + Fore.RESET + 
                      " Time: " + str(end_char_time))
                count_right += 1
                cumTimeRight += end_char_time
                
            elif input_key != chr(random_char):
                end_char_time = time() - init_char_time
                print(input_key + Fore.RED + " Wrong key " + Fore.RESET + 
                      " Time: " + str(end_char_time))
                count_wrong += 1
                cumTimeWrong += end_char_time

            #Adding the values to the list
            list_inputs.append(Input(chr(random_char), input_key, "%.2f" %end_char_time))

            cumTime += end_char_time
            count = count_right + count_wrong

            if count == num_inputs:
                end_game_time = ctime()
                end_time = time() - init_time
                break

        dataGame(count, end_time, count_right, (count_right/count), (cumTime/end_time),
                (cumTimeRight/end_time), (cumTimeWrong/end_time), init_game_time, end_game_time, list_inputs)
    

    #Time Mode for Characters    
    else:

        init_time = time()

        
        while (True):

            #Generating numbers --> chr() to convert in letters

            random_char = random.randint(97, 122)
            init_char_time = time()
            print(chr(random_char))
            input_key = readkey()

            # Defining space to quit the game 
            if input_key == ' ':
                break
            
            # Verification of the typing 
            elif input_key == chr(random_char):
                end_char_time = time() - init_char_time
                print(input_key + Fore.GREEN + " Correct key " + Fore.RESET + 
                      " Time: " + str(end_char_time) + " seconds")
                count_right += 1
                cumTimeRight += end_char_time
                

            # Verification of the typing mistake 
            elif input_key != chr(random_char):
                end_char_time = time() - init_char_time
                print(input_key + Fore.RED + " Wrong key " + Fore.RESET + 
                      " Time: " + str(end_char_time) + " seconds")
                count_wrong += 1
                cumTimeWrong += end_char_time

            #Adding the values to the list
            list_inputs.append(Input(chr(random_char), input_key, "%.2f" %end_char_time))

            cumTime += end_char_time
            count = count_right + count_wrong

            end_time = time() - init_time

            end_game_time = ctime()

            
            if end_time >= num_inputs:
                break

        print("Time finished you printed: " + str(count_right) + " characters right!!")

        dataGame(count, end_time, count_right, (count_right/count), (cumTime/end_time), 
                (cumTimeRight/end_time),(cumTimeWrong/end_time), init_game_time, end_game_time, list_inputs)



# Word Function
def mod_word(num_inputs, mode):

    """This function is only for Word Mode. 

    Args:
        num_inputs: value set on MAX_VALUE (in arguments funcion)

        mode: value se
    Value:

    """
    
    randomwords = RandomWords()
    compare_word = ""
    #compare_word = []
    """count = 0
    count_right = 0
    count_wrong = 0
    cumTime = 0
    cumTimeRight = 0
    cumTimeWrong = 0
    init_game_time = ctime()
    end_game_time = 0
    end_time = 0"""
    exit_key = ""
    #exit_key = []
    #random_word = []

    # Input Mode for Words
    if mode == 'inputs':
        init_time = time()

        while(True):
            random_word = randomwords.get_random_word()
            #random_word.append(randomwords.get_random_word())
            
            print(random_word)
            init_word_time = time()

            while (True):
                exit_key = readkey()
                #exit_key = input()
                
                if exit_key == ' ':
                    break

                else:
                    compare_word += exit_key
                    #compare_word = compare_word.append(exit_key)
                    


                    if(len(compare_word) == len(random_word)):

                        if compare_word == random_word:
                            end_word_time = time() - init_word_time
                            print(compare_word + Fore.GREEN + " Correct word " + Fore.RESET + 
                                " Time: " + str(end_word_time) + " seconds")
                            count_right += 1
                            cumTimeRight += end_word_time
                            
                        elif compare_word != random_word:
                            end_word_time = time() - init_word_time
                            print(compare_word + Fore.RED + " Wrong word " + Fore.RESET + 
                                " Time: " + str(end_word_time) + " seconds")
                            count_wrong += 1
                            cumTimeWrong += end_word_time


                        cumTime += end_word_time

                        #Adding the values to the list
                        list_inputs.append(Input(random_word, compare_word, "%.2f" %end_word_time))

                        count = count_right + count_wrong
                        compare_word = ""
                        break

            if count == num_inputs or exit_key == ' ':
                end_game_time = ctime()
                end_time = time() - init_time
                break

        dataGame(count, end_time, count_right, (count_right/count), (cumTime/end_time),
                (cumTimeRight/end_time), (cumTimeWrong/end_time), init_game_time, end_game_time, list_inputs)

    # Time Modo for Words
    else:
        init_time = time()

        while(True):
            random_word = randomwords.get_random_word()
            print(random_word)
            init_word_time = time()

            while(True):
                exit_key = readkey()
                
                            
                if exit_key == ' ':
                    break

                else:
                    compare_word += exit_key

                    if(len(compare_word) == len(random_word)):


                        if compare_word == random_word:

                            end_word_time = time() - init_word_time
                            print(compare_word + Fore.GREEN + " Correct word " + Fore.RESET + 
                                " Time: " + str(end_word_time) + " seconds")
                            count_right += 1
                            cumTimeRight += end_word_time
                            
                            
                        elif compare_word != random_word:
                            end_word_time = time() - init_word_time
                            print(compare_word + Fore.RED + " Wrong word " + Fore.RESET + 
                                " Time: " + str(end_word_time) + " seconds")
                            count_wrong += 1
                            cumTimeWrong += end_word_time

                        #Adding the values to the list
                        list_inputs.append(Input(random_word, compare_word, "%.2f" %end_word_time))

                        cumTime += end_word_time
                        count = count_right + count_wrong
                        compare_word = ""

                        break
                
                end_time = time() - init_time

                if end_time >= num_inputs:
                    break

            if end_time >= num_inputs or exit_key == ' ':
                end_game_time = ctime()
                break
        
        print("Time finished you printed: " + str(count_right) + " words right!!")

        
        dataGame(count, end_time, count_right, (count_right/count), (cumTime/end_time),
                (cumTimeRight/end_time), (cumTimeWrong/end_time), init_game_time, end_game_time, list_inputs)    


def dataGame(num_inputs, testTime, inputRight, inputAccuracy, timeAVG, inputRightTimeAVG, inputWrongTimeAVG, startTime, endTime, inputTuples):
    """This functiion is only to store the final results of the game.

    
    Args: 
            num_inputs: The total amount of the user input.
            testTime:
            inputRight:
            inputAccuracy:
            timeAVG:
            inputRightTimeAVG:
            inputWrongTimeAVG: 
            startTime: 
            endTime:
            inputTuples:
    """
    data = {'accuracy': inputAccuracy,
            'inputs':inputTuples,
            'number_of_hits': inputRight,
            'number_of_types': num_inputs,
            'test_duration': "%.2f" %testTime,
            'test_start': startTime,
            'test end': endTime,
            'type_average_duration': "%.2f" %timeAVG,
            'type_hit_average_duration': "%.2f" %inputRightTimeAVG,
            'type_miss_average_duration': "%.2f" %inputWrongTimeAVG}
    
    pprint(data)

def main():
    arguments()

if __name__ == "__main__":
    main()