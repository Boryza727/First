print("Hello! My name is Aid")
print("I was created in 2020")
print("Please, remind me your name")
name = str(input())
print("What a great name you have, " + str(name) + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is ", age, "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
n = 0
while n <= number:
    print(n, "!")
    n += 1
print("Completed, have a nice day!")
