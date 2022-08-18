counter = 0
print("Count of recursive calls you want to make: ")
recursiveCallsCount = int(input())


def recurseMe():
    global counter
    print(counter, ". I am from Mars!")
    counter = counter + 1
    #define the stop condition for recursion
    if(counter == recursiveCallsCount):
        return 1
    #function will call itself again
    recurseMe()


#below function will be called
recurseMe()
