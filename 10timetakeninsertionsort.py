import time
import random


print("What array size do you want to generate?")
size  = int(input())

scores = []

def generateArray(n):
    counter = 0
    while(counter < n):
        randomNumber = random.randint(0,size)
        scores.append(randomNumber)
        counter = counter + 1
        

def insertionSort(receivedScores):
    for counter in range(1, len(receivedScores)):
        #print(counter)
        index = receivedScores[counter]
        j = counter - 1
        
        while( j >= 0 and index < receivedScores[j]):
            receivedScores[j+1]=receivedScores[j]
            j = j - 1
        receivedScores[j+1] = index        
        
        
generateArray(size)
print("Size of generated array: ")
print(len(scores))

startTime = time.time()
insertionSort(scores)
endTime = time.time()
print("Time taken: ", endTime - startTime )        