import time

startTime = time.time()
counter = 0
anotherCounter = 0
testVariable1 = 0
testVariable2 = 0
testVariable3 = 0
testVariable4 = 0
testVariable5 = 0
testVariable6 = 0
testVariable7 = 0
testVariable8 = 0

maxCounter = 100000
while(counter < maxCounter):
    counter = counter + 1
    anotherCounter = 0
    #print(counter)
    # while(anotherCounter < maxCounter):
    #     anotherCounter = anotherCounter + 1


endTime = time.time()
print("Time taken: ", endTime - startTime)
