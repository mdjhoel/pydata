print("Hello cruel world. I watching you")

age = 53 # this is an integer
pi = 3.14 # this is a float
name = "Mark" # string
iscool = True # boolean

print(age+pi)
print(age - pi)
print(age / pi)
print(age * pi)
niceoutput = round(age * pi,1)
print(niceoutput)

print("Your name is " + name + " and your age is " + str(age))

# sequential, selection, repetition

myage = input("What is your age?: ")
if(int(myage) >= 50):
    print("you are old")
elif(int(myage) <= 19 and int(myage) >= 13):
    print("I am a teen")
else:
    print("you are young")



