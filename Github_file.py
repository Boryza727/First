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
print("Now I will prove to you that I can count to any number you want. Insert a number: ")
number = int(input())
n = 0
while n <= number:
    print(n, "!")
    n += 1
print("Completed, have a nice day IN A NEW BRANCH! ")
print()
print("Choose one of these words: ", "aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac")
dictionary = ["aa", "aac", "bac", "baba", "caac"]
word = str(input())
if word in dictionary:
    print("This word is in dictionary")
else:
    print("This word is NOT in dictionary")
print()
print("Choose a year to check whether it is leap or ordinary")
year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print("Leap")
elif year % 200 == 0:
    print("Leap")
else:
    print("Ordinary")
    
traffic_lights = ["green", "yellow", "red"]
print("What colour do you see: green, yellow, red, or violet?")
light = str(input())  # variable for color name
if light in traffic_lights:
    print("co sie stanie?")
    if light == "green":
        print("You can go!")
    elif light == "yellow":
        print("Get ready!")
    else:
        # if the lights are red
        print("Just wait.")
else:
    print("No such traffic light color, do whatever you want")
