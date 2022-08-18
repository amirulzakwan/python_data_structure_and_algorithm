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


def partitionAndOrganize(array, leftPosition, rightPosition):
    #assume right most as pivot
    pivot = array[rightPosition]
    
    #assumed postion for greater number
    i = leftPosition - 1
    
    #loop through all elements in array
    #compare each element with pivot
    for check in range(leftPosition, rightPosition):
        if(array[check] <= pivot):
            #if array[check] is smaller than pivot
            #swap it with greater element pointed by i
            i = i + 1
            #do swapping
            (array[i], array[check])=(array[check], array[i])
    
    #swap the element at pivot position with greater element at i positoin
    (array[i+1], array[rightPosition])=(array[rightPosition], array[i+1])        

    #sleep(10)
    #print("in partition-------------------------")
    #print(array)
    #print()
    
    #return the position where partition happened
    return  i+1


#do the partition for quicksort
def quickSort(myScores, left, right):
    if(left < right):
        
        #find the pivot such that
        #all the elements greater than the pivot
        #are on right and all the elements smaller
        #then pivot are on left
        pivotPosition = partitionAndOrganize(myScores, left, right)
        
        #call quickSort recursively for array on left of pivotPostion
        quickSort(myScores, left, pivotPosition -1)
        #call quickSort recursively for array on right of pivotPostion        
        quickSort(myScores, pivotPosition + 1, right)
        

        
   

#scores = [7, 6, 13, 11, 10, 2, 1, 18, 22, 17, 14]
#print("Unsorted list:")
#print(scores)
generateArray(size)
print("Size of generated array: ")
print(len(scores))

startTime = time.time()
quickSort(scores, 0, len(scores)-1)
endTime = time.time()
print("Time taken: ", endTime - startTime )
