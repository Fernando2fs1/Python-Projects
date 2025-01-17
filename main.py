from operator import truediv

print("Hello World")
print ("this is a test ")
print ("testing my python skills")

nameCheck = True

x = 10
y = 20
my_name = "Fernando"

sum = x + y

print ("the result of the sum is ", sum)

div = y / x

print ("the result of the division is ", div)

sub = y - x

print ("the resul of the subtraction is ", sub)

mul = x * y

print ("the result of the multiplication is ", mul)


if my_name == "Fernando":
    print("Hello Fernando")

if my_name == "Fernando":
    print (x)

if my_name == "Fernando":
    nameCheck = True
    print ("that is the correct name")
else:
    nameCheck = False
    print ("That is the wrong name")


name = input("Enter your name:")
print("nice to meet you ", name)

age = int(input("how old are you?"))
if age >= 18:
    print("you are an adult.")
else:
    print("you are still a child")
