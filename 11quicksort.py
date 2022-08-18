from time import sleep


def partitionAndOrganize(array, leftPosition, rightPosition):
    # assume right most as pivot
    pivot = array[rightPosition]

    # assume position for greater number
    i = leftPosition - 1

    # loop through all elements in array
    # compare each element with pivot
    for check in range (leftPosition, rightPosition):
        if(array[check] <= pivot):
            # if array[check] is smaller than pivot
            # swap it with the greater element pointed by i
            i = i + 1
            # do swapping
            (array[i], array[check])=(array[check], array[i])
    # swap the element at pivot position with greater element at i position
    (array[i+1], array[rightPosition])=(array[rightPosition], array[i+1])

    sleep(2)
    print("in partition-----------------------------")
    print(array)

    # return the position where partition happend
    return i+1



# do the partition for quicksort
def quickSort(myScores, left, right):
    if(left < right):

        # find the pivot such that
        # all the elements greater than the pivot
        # are on left and all the elements smaller
        # then pivot are on right
        pivotPosition = partitionAndOrganize(myScores, left, right)

        # call quickSort recursively for array on left of pivotPosition
        quickSort(myScores, left, pivotPosition -1)
        # call quickSort recursively for array on left of pivotPosition
        quickSort(myScores, pivotPosition + 1, right)




scores = [7, 6, 13, 11, 10, 2, 1, 18, 22, 17, 14]
print("Unsorted list:")
print(scores)

lengthOfScores = len(scores)
# 0 is position on left
# lengthOfScores-1 is position on right
quickSort(scores, 0, lengthOfScores-1)