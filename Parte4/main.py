#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

#from my_fun import 
               
import time
import random
from threading import Timer                  # This will allow to compute more than one chore at the same time
from colorama import Fore, Back, Style
import argparse

# define functions here ...

class TypingGame():
     
     def __init__(self):#, max_input, time_input):
          
          self.timestamps = []
          
          self.timestamps.append(time.asctime())
          print(self.timestamps)


          self.open_text = open("text.txt", "r").read().split("\n")

          
          self.start_time = time.time()

          #criar ciclo while
          while timeout == False:
               self.ReadText()
               self.Timefunc()
          #fora do ciclo while

          self.end_time = time.time()

          self.time_taken = self.end_time - self.start_time
          

     
     def ReadText(self):

          self.phrase = random.choice(self.open_text)
          self.wordcount = self.phrase.split(" ")

          print(self.phrase)
          #len(self.phrase)
          #print(self.wordcount)
          

          

     def Timefunc(self):
          
          words = []

          fail_words =[]
          correct_words = []

          # start_variável_cronômetro 
         
          self.inputext = str(input('Enter the Sentece: \n'))
          
          for word in range(len(self.inputext)):

               if self.inputext[word] != self.wordcount:

                    words.extend((self.inputext,word))      
                    print(Fore.RED + words + Style.RESET_ALL)

                    fail_words.append(self.inputext)


               else:
                    words.extend((self.inputext,word))      
                    print(Fore.GREEN + words + Style.RESET_ALL)

                    correct_words.append(self.inputext)
               
               accuracy = len(correct_words) / len(words)

               self.wpm = self.wordcount / self.time_taken * accuracy

               print(f"WPM,{self.wpm :.2f}, Accuracy: {accuracy :.2f},Time taken: {self.time_taken :.2f}")


               
          
     """def statistics(self):

          #accuracy = len(set(self.inputext.split()) & set(self.phrase))
          #accuracy = accuracy/self.wordcount

          time_taken = []  
          #self.end_time - self.start_time

          

          print(f"WPM,{wpm :.2f}, Accuracy: {accuracy :.2f},Time taken: {time_taken :.2f}")"""
                    


def main():
          
     """parser = argparse.ArgumentParser(description='Description of your program')
     #parser.add_argument('-h','--help', help='Description for foo argument', required=False)
     parser.add_argument('-utm','--use_time_mode', help='Description for foo argument', required=False)
     parser.add_argument('-mv','--max_value', help='Description for bar argument', required=False)
     args = parser.parse_args()

     
     max_input = args.max_value
     time_input = args.use_time_mode


     if max_input is not None:
          max_input = int(max_input)

     elif time_input is not None:
          time_input = int(time_input)

     else:
          print('Enter an argument (-mv, -utm, -h) + space and a number')

    """ """elif help_input is not None:
          help_input ="""  """
     
     input('Press enter to continue: ')
     print(type(max_input))

     class_object = TypingGame(max_input, time_input)
     #class_object()

     while True:
          class_object.ReadText()"""
     

if time_input:

     timeout = int(input("Enter an timer: "))
     t = Timer(timeout, print("Time's up!"))

     t.start()
     TypingGame()

TypingGame()


if __name__ == "__main__":
    main()