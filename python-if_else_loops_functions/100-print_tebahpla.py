#!/usr/bin/python3
for i in range(25, -1, -1):
    print(chr(i + 97) if i % 2 == 0 else chr(i + 65), end="")

