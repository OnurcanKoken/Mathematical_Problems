from circle import *
# from is much more useful
import circle as asdfg

asdfg.hello()
hello()
area(5)
print(asdfg.pi)
print(asdfg.circumference(3))

nameHandle = open('kids', 'w')
#creates a new file, it is opened for writing into / file handle
for i in range (2):
    name = input("Enter name: ")
    nameHandle.write(name + '\ ' )
nameHandle.close()
