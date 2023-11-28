#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            if i < 9:
                print("{:d}{:d}, ".format(i, j), end='')
            else:
                print("{:d}{:d}".format(i, j))

print()  # Add a newline at the end
