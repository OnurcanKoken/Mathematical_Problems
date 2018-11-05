# problem 1.3
s = 'azcbobobegghakl'
temp = " "
result = " "

for c in s:
    if len(temp) == 0 or c >= temp[-1]:
        temp += c
    else:
        temp = c
    if len(temp) > len(result):
        result = temp
print("Longest substring in alphabetical order is: ", result)