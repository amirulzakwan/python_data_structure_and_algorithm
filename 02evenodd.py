# checkNumber = 21
# take input from user
print("Input any number: ")
inputNumber = input()
# datatype of typing any input at command line is always string
print("Your input is ", inputNumber)
checkNumber = int(inputNumber)
if(checkNumber%2 == 0):
    print(checkNumber, " is even.")
else:
    print(checkNumber, " is odd.")