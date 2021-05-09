# köken
# date: 19.02.2021 (dd/mm/yyyy)

# number of strings
T = int(input())
A = []
# insert given strings into an array
for i in range(0,T):
    temp = input()
    A.append(temp)
cnt_T = 0

while(True):
    temp_str = A[cnt_T]
    chr_j = 0
    temp_temp_str_1 = ""
    for chr_i in temp_str:
        if chr_j % 2 == 0:
            temp_temp_str_1 = temp_temp_str_1 + chr_i
        chr_j += 1
    chr_j = 0
    temp_temp_str_2 = ""
    for chr_i in temp_str:
        if chr_j % 2 == 1:
            temp_temp_str_2 = temp_temp_str_2 + chr_i
        chr_j += 1
    print(temp_temp_str_1 + " " + temp_temp_str_2)
    cnt_T += 1
    if cnt_T == T:
        break