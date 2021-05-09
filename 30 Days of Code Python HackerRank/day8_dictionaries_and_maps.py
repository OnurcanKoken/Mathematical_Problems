# köken
# date: 21.02.2021 (dd/mm/yyyy)

# more detail: https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries
# reference: https://stackoverflow.com/questions/44495647/hackerrank-day-8-python/49487826

# get the number of keys
key_value = int(input())
# create dictionary
phoneBook = {}

# get the keys and their related numbers
for i in range(0,key_value):
    # get raw data, multiple variable at once
    key, key_num = [str(x) for x in input().split()]
    key, key_num = [str(key), str(key_num)]
    # add a new key
    phoneBook[key] = key_num

# check
while True:
    try:
        # ask for the key
        ask_key = str(input())

        if ask_key in phoneBook:
            # print the corresponding number for the given key
            print(ask_key + "=" + phoneBook[ask_key])
        else:
            print("Not found")
    except EOFError:
        break