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

generateArray(size)
print("Generated array: ")
#print(scores)
print("Size of generated array: ")
print(len(scores))

startTime = time.time()
scores.sort()
endTime = time.time()
print("Time taken: ", endTime - startTime)
#print("Sorted scores: ")
#print(scores)
