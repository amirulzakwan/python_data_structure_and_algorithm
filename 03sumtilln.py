print("Input any number (to find sum of all numbers till n): ")

inputNumber = int(input())

print("Sum of all numbers till ", inputNumber )

#intial sum is zero
sum = 0

#use counter variable as a stop condition in loop so that
#computer stops after calcualting the sum of all numbers till inputNumber
counter = 0

#use while loop
while(counter < inputNumber):
    sum = sum + counter
    counter = counter + 1
print ("Sum of all numbers till ", inputNumber , " is " , sum)

