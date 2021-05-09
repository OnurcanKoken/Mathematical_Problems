# köken
# date: 01.03.2021 (dd/mm/yyyy)
# check Handling Exceptions part of https://docs.python.org/3/tutorial/errors.html

import sys

S = input().strip()
try:
    int(S)
    print(S)
except ValueError:
    print("Bad String")
