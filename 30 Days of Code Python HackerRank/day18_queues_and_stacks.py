# köken
# date: 26.04.2021 (dd/mm/yyyy)
# Stacks and Queues
# A palindrome is a word, phrase, number, or other sequence of characters
# which reads the same backwards and forwards.
import sys

class Solution:
    def __init__(self):
        # stacks Last-In-First-Out (LIFO)
        # add an object passed as an argument to the top of the stack
        # stack_push = []
        # remove the object at the top of the stack and return it
        # stack_pop = []

        self.stack = []

        # queues First-In-First-Out (FIFO)
        # enqueue: Add an object to the back of the line
        # pop_queue_chr = []
        # dequeue: Remove the object at the head of the line and return it
        # push_dequeue_chr = []

        self.queue = []

    def pushCharacter(self, s_chr):
        # push, insert
        self.stack.append(s_chr)

    def enqueueCharacter(self, s_chr):
        # enqueue, add an object to the back of the line
        self.queue.append(s_chr)

    def popCharacter(self):
        # take out
        first_chr = self.stack.pop()
        return first_chr

    def dequeueCharacter(self):
        # dequeue, remove the object at the head of the line and return it
        last_chr = self.queue.pop(0)
        return last_chr

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")

'''
references:
https://www.hackerrank.com/challenges/30-queues-stacks/problem
https://stackabuse.com/stacks-and-queues-in-python/
'''