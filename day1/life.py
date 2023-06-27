print("hello world")


def tellme(age):
    status = "kid"
    if (age < 13):
        status = "kid"
    elif (age >= 13 and age < 20):
        status = "teen"
    elif (age > 19 and age <= 30):
        status = "young adult"
    else:
        status = "adult"
    return status

def friendcount():
    import random
    print("This app will count your friends and give a witty quip. Type 'q' to quit.")

    witisisms = ["People named this are usually stuck up", "Nice name", "Umm, who would call their kid that", "I like that one"]
    friends = []
    keepgoing = True
    while keepgoing == True:
        friend = input("Type in a friends' name and click enter: \n")
        if (friend == 'q'):
            print("Good bye. You have " + str(len(friends)) + " friends")
            keepgoing = False
        else:
            friends.append(friend)
            print(random.choice(witisisms))
        

'''
    SSRGMIO - sequence, select, repeat, graphics, modular, file IO
    data variables, integer, string data, math operations,
    if statement, comparison operators
    string concatenation, built in functions, type casting
    Python blocks (functions, if, loops use indentation)
    Make and call a function that returns a value
    lists and loops if time permits, booleans, while loop
'''

lifeex = 82 # Canada's life expectancy - this is a comment
age = input("How old are you now: ") # user input stored in string var
timeleft = lifeex - int(age) # do math, must change age to number
# now, give output. use string concatenation and change number to string
print("Thanks, you are currently " + age + ".\nYou have " + str(timeleft) + " years left to live")
mystatus = tellme(int(age))
print("You are currently a " + mystatus)

#friendcount()



    
