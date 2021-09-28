# Count Digits 8
# 28.09.2021
# Onurcan Köken

def countDigits(array_j):
    # number of digits in j
    num_dig = 0
    list_dig = []
    for i in (array_j):
        num_dig = 0
        for k in str(i):
            if int(k) == 0:
                continue
            if (i%int(k)) == 0:
                num_dig = num_dig + 1
            #print(k) # each digit in a number is "k"
        #print(i) # each number is "i"
        print(num_dig)
        list_dig.append(int(num_dig))
    # return the number of digits in j that are divisors of j
    return list_dig

t = int(input("Enter the number of test cases: "))
list_numbers = []
for i in range(t):
    list_numbers.append(int(input()))

print(countDigits(list_numbers))