

from errno import EACCES


def insertionSort(receivedScores):
    for counter in range(1, len(receivedScores)):
        #print(counter)
        index = receivedScores[counter]
        j = counter - 1

        while(j >= 0 and index < receivedScores[j]):
            receivedScores[j+1] = receivedScores[j]
            j = j - 1
        receivedScores[j+1] = index


scores = [7, 6, 13, 11, 10, 2, 1, 18, 22, 17, 14]
print("Unsorted list:")
print(scores)

insertionSort(scores)
print("Sorted: ")
print(scores)
