# köken
# date: 25.02.2021 (dd/mm/yyyy)
# reference: https://www.codesadda.com/hr/30-days/python/Python%20Day%2012:%20Inheritance/
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here

    def calculate(self):
        sub = 0
        grade = 0
        for i in self.scores:
            sub += i
        grade = sub/len(self.scores)

        if 90 <= grade <= 100:
            return 'O'
        elif 80 <= grade < 90:
            return 'E'
        elif 70 <= grade < 80:
            return 'A'
        elif 55 <= grade < 70:
            return 'P'
        elif 40 <= grade < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
