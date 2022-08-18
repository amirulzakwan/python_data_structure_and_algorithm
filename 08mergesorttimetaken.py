import time
import random


print("What array size do you want to generate?")
size = int(input())

scores = []


def generateArray(n):
    counter = 0
    while(counter < n):
        randomNumber = random.randint(0, size)
        scores.append(randomNumber)
        counter = counter + 1


def mergeSort(receivedScores):
    if(len(receivedScores) > 1):
        #print("Received scores")
        #print(receivedScores)
        #divide received scores in 2 half

        #identify middlePosition for dividing recivedScores in 2 half
        middlePosition = int(len(receivedScores)/2)
        #create 1st half from the left side of middlePosition
        leftScores = receivedScores[:middlePosition]
        #create 2nd half from the right side of middlePosition
        rightScores = receivedScores[middlePosition:]
        #print("Left scores: ")
        #print(leftScores)
        #print("Right scores: ")
        #print(rightScores)
        #print("--------------------------------------------")
        #keep dividing receivedScores recursively till there is only
        #one element left in receivedScores

        #pass leftScores to mergeSort to trigger the recursive call
        mergeSort(leftScores)
        #pass rightScores to mergeSort to trigger the recursive call
        mergeSort(rightScores)

        #start merging
        #use 3 variables for task of position shift while merging
        i = 0
        j = 0
        k = 0
        #print("############################################")
        #print("Merging to start now: ")

        #pick the less value from ith position from
        #leftScores and rightScores
        while(i < len(leftScores) and j < len(rightScores)):
            if(leftScores[i] < rightScores[j]):
                #the value from leftScores is used
                receivedScores[k] = leftScores[i]
                #move the position in leftScores forward by 1 step
                i += 1
            else:
                #the value from rightScores is used
                receivedScores[k] = rightScores[j]
                #move the position in rightScores forward by 1 step
                j += 1

            #move to the next position in receivedScores array
            k += 1
           #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
           #print(leftScores)
           #print(rightScores)
           #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        while(i < len(leftScores)):
            receivedScores[k] = leftScores[i]
            i += 1
            k += 1

        while(j < len(rightScores)):
            receivedScores[k] = rightScores[j]
            k += 1
            j += 1


#scores = [7, 6, 13, 11, 10, 2, 1, 18, 22, 17, 14]
#print("Unsorted list:")
#print(scores)
generateArray(size)
print("Size of generated array: ")
print(len(scores))

startTime = time.time()
mergeSort(scores)
# print("Sorted: ")
# print(scores)
endTime = time.time()
print("Time taken: ", endTime - startTime)
