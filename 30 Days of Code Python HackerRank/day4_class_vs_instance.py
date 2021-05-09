# köken
# date: 17.02.2021 (dd/mm/yyyy)

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 1:
            print("Age is not valid, setting age to 0.")
            initialAge = 0
        self.Age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.Age < 13:
            print("You are young.")
        elif self.Age > 12 and self.Age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.Age += 1

t = int(input())