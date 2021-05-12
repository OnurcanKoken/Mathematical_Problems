# Reference: https://www.geeksforgeeks.org/reading-writing-text-files-python/

# Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file.
# If the file does not exists, raises I/O error. This is also the default mode in which file is opened.

# Read and Write (‘r+’) : Open the file for reading and writing.
# The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.

# Write Only (‘w’) : Open the file for writing. For existing file, the data is truncated and over-written.
# The handle is positioned at the beginning of the file. Creates the file if the file does not exists.

# Write and Read (‘w+’) : Open the file for reading and writing.
# For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.

# Append Only (‘a’) : Open the file for writing. The file is created if it does not exist.
# The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

# Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist.
# The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

# Python program to illustrate
# Append vs write mode
file1 = open("new_file.txt", "w")
L = ["This is Istanbul \n", "This is Angara \n", "This is Ckale \n"]
file1.close()

# Append-adds at last
file1 = open("new_file.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("new_file.txt", "a")  # append mode
file1.write("Today \n")


for i in range(0,10):
    file1 = open("new_file.txt", "a")  # append mode
    file1.write(str(i) + "\n")

# file1 = open("myfile.txt", "r")
# print
# "Output of Readlines after appending"
# print
# file1.readlines()
# print
# file1.close()
#
# # Write-Overwrites
# file1 = open("myfile.txt", "w")  # write mode
# file1.write("Tomorrow \n")
# file1.close()
#
# file1 = open("myfile.txt", "r")
# print
# "Output of Readlines after writing"
# print
# file1.readlines()
# print
# file1.close()