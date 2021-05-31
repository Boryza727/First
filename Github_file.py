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
    
print("How many animals you can afford? ")
print("indicate the amount to spend")
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
Sum = int(input())
if (Sum / sheep) >= 1:
    if (Sum / sheep) >= 2:
        print(int(Sum / sheep), str("sheep"))
    else:
        print(int(Sum / sheep), str("sheep"))
elif (Sum / cow) >= 1:
    if (Sum / cow) >= 2:
        print(int(Sum / cow), str("cows"))
    else:
        print(int(Sum / cow), str("cow"))
elif (Sum / pig) >= 1:
    if (Sum / pig) >= 2:
        print(int(Sum / pig), str("pigs"))
    else:
        print(int(Sum / pig), str("pig"))
elif (Sum / goat) >= 1:
    if (Sum / goat) >= 2:
        print(int(Sum / goat), str("goats"))
    else:
        print(int(Sum / goat), str("goat"))
elif Sum / chicken >= 1:
    if (Sum / chicken) >= 2:
        print(int(Sum / chicken), str("chickens"))
    else:
        print(int(Sum / chicken), str("chicken"))
elif (Sum / chicken) < 1:
    print("None")

#  AXIS
x = float(input())
y = float(input())
if x == 0 or y == 0:
    print("It's the origin!" if x == 0 and y == 0 else "One of the coordinates is equal to zero!")
elif x > 0:
    print("I" if y > 0 else "IV")
elif x < 0:
    print("II" if y > 0 else "III")

 #  FUNCTION DEFINITION AND INFOKING   
def calculator(x, y, operation):
    if (operation == "/" and y == 0.0) or (operation == "mod" and y == 0.0) or (operation == "div" and y == 0.0):
        print("Division by 0!")
    elif operation == "+":
        print(x + y)
    elif operation == "-":
        print(x - y)
    elif operation == "/":
        print(x / y)
    elif operation == "*":
        print(x * y)
    elif operation == "mod":
        print(x % y)
    elif operation == "pow":
        print(x ** y)
    elif operation == "div":
        print(x // y)
calculator(5, 10, "*")

# RANDOM SEED
import random
n = int(input())
random.seed(n)
print(random.choice("Voldemort"))

# YODA STYLE
import random

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
random.seed(43)
random.shuffle(sentence)
# shows the message
print(' '.join(sentence))

# Random
import random
print("H A N G M A N")
print("Guess the word:")
x = str(input())
words = ['python', 'java', 'kotlin', 'javascript']
random.seed()
y = random.choice(words)
if x == y:
    print("You survived!")
else:
    print("You lost!")
    
    
# `random + while
import random
print("H A N G M A N")
print("Guess the word:")
words = ['python', 'java', 'kotlin', 'javascript']
while 1 > 0:
    random.seed()
    y = random.choice(words)
    x = str(input())
    if x == y:
        print("You survived!")
        break
    else:
        print("You lost! Try one more time")
    continue

    
# DYNAMICZNE WSTAWIANIE TEKSTU
nickname = input()
profession = input()
print(f'http://example.com/{nickname}/desirable/{profession}/profile')

# PARSING
word = input()
print(word.strip("*_~`"))

print(message.replace("Paris", "Lyon"))  # bonjour and welcome to Lyon!
replaced_message = message.replace("o", "!", 2)


whitespace_string = "     hey      "
normal_string = "incomprehensibilities"

# delete spaces from the left side
whitespace_string.lstrip()  # "hey      "

# delete all "i" and "s" from the left side
normal_string.lstrip("is")  # "ncomprehensibilities"

# delete spaces from the right side
whitespace_string.rstrip()  # "     hey"

# delete all "i" and "s" from the right side
normal_string.rstrip("is")  # "incomprehensibilitie"

# no spaces from both sides
whitespace_string.strip()  # "hey"

# delete all trailing "i" and "s" from both sides
normal_string.strip("is")  # "ncomprehensibilitie"

# USUWANIE POSZCZEGÓLNYCH ZNAKÓW JEDNĄ LINIJKĄ
text = input()
for i in "?!,.":
    text = text.replace(i, "")
print(text.lower())

# USUWANIE ZNAKÓW W PROSTY SPOSÓB
text = input()
text = text.lower()

symbols = ",;:.¡!¿?@/*-+_"
for char in symbols:
    text = text.replace(char, '')

print(text)

# ZAOKRĄGLANIE DO "F" MIEJSC PO PRZECINKU.
amount = 3.252537
print(f"The tax for {amount:.5f} dollars!")


def check_email(string):
    n = string.find("@")
    if " " in string:
        return False
    elif "@." in string:
        return False
    elif "." not in string:
        return False
    elif "." not in string[n:]:
        return False
    else:
        return True
print(check_email(input()))

# HANGMAN CD.
import random
print("H A N G M A N")
word = ["python", "java", "kotlin", "javascript"]
random.seed()
x = random.choice(word)
y = len(x)
z = y - 3
print("Guess the word", x[0:3]+(z*"-")+":")
guess = input()
if guess == x:
    print("You survived!")
else:
    print("You lost!")
    
    

