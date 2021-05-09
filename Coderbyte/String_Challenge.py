"""
run-length encoding algorithm
takes the occurrence of each repeating character
outputs the number along with a single character of the repeating sequence

For example: "wwwggopp" would return 3w2g1o2p
The given string will not contain any numbers,
punctuation, or symbols

Another example: "aabbcde" would return 2a2b1c1d1e
Another example: "wwwbbbw" would return 3w3b1w

Coderbyte String Challenge Question

Onurcan Köken
19.04.2021
"""

def StringChallenge(given_word):
    # current character of the given word
    current_chr = given_word[0]
    # temporary previous character
    previous_chr = ""
    # count the repeated characters
    counter = 1
    # empty encoded version of the given_word
    encoded_str = ""
    if len(given_word) == 0:
        print("empty")
    # if only 1 character is entered
    elif len(given_word) == 1:
        print(str(1) + given_word[0])
    # actual case
    else:
        for i in range(len(given_word)):
            current_chr = given_word[i]
            # compare current and previous characters
            # and count if it is the same
            if current_chr == previous_chr:
                counter = counter + 1
            # the character is changed, so:
            else:
                # if the first character and second character are different
                if i == 0:
                    previous_chr = given_word[i]
                    continue
                # increase the counter if previous and current characters are the same
                encoded_str = encoded_str + str(counter) + previous_chr
                counter = 1
            # update the previous character
            previous_chr = given_word[i]
        # append necessary number of repetitions with the characters here at the end
        if given_word[len(given_word) - 1] != given_word[len(given_word) - 2]:
            encoded_str = encoded_str + str(1) + previous_chr
        if given_word[len(given_word) - 1] == given_word[len(given_word) - 2]:
            encoded_str = encoded_str + str(counter) + previous_chr
        # print the encoded result
        print(encoded_str)
    # no need to return something
    return None
# test the encoding
while True:
    StringChallenge(input("Enter a word: "))