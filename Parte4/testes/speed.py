## teste 3

import time

string = ' aqui é um teste, tem que escrever frases de várias formas diferentes.'
wordcount = len(string.split())

print(string)

while True:
    start_time = time.time()
    inputext = str(input('Enter the Sentece: \n'))
    end_time = time.time()
    
    accuracy = len(set(inputext.split()) & set(string.split()))
    accuracy = accuracy/wordcount
    
    time_taken = end_time - start_time 

    wpm = wordcount / time_taken

    print(f"WPM,{wpm :.2f}, Accuracy: {accuracy :.2f},Time taken: {time_taken :.2f}")
