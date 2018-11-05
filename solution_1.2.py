s = 'azcbobobegghbobobobobakl'
i = 0
a = 0
for n in s:
    if n == "b" and s[i+1] == "o" and s[i+2] == "b":
        a += 1
    i += 1
print("Number of times bob occurs is: ", a)