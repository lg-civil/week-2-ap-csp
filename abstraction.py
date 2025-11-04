# abstraction is when I hide 
# the complex details for something
# a lot more simple. 

# personal infor
# a function allows us to wrap data or 
# information into a special box or
# enclosure fore reuse
# define a function
def personaInformation():
    question1 = input("How old are you?")
    question2 = input("Where do you live")
    question3 = input("What school do you go to?")
    print(question1 + question2 + question3)

# call the function

# personaInformation()
# personaInformation()
# personaInformation()

# make a function that guesses how old you are

def age():
    q1 = int(input("What year is it now? "))
    q2 = int(input("What year were you born? "))
    answer = q1 - q2
    result = print(f"you are {answer} years old.")

age()
age()
age()