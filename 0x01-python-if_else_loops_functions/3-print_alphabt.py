#!/usr/bin/python3

for i in range(97, 123):
    if i != 101 and i != 113:  # ASCII values for 'e' and 'q'
        print("{}".format(chr(i)), end='')

print()  # Add a newline at the end
