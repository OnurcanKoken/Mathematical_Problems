nameHandle = open("kids", "r")
for line in nameHandle:
    print(line)
nameHandle.close()

"""
nameHandle = open('kids', 'w')
#creates a new file, it is opened for writing into / file handle
for i in range (2):
    name = input("Enter name: ")
    nameHandle.write(name + '\ ' )
nameHandle.close()
"""