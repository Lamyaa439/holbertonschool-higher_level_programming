#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numbers = sys.argv
    len_list = len(numbers)
    result = 0
    for i in range(1, len_list):
        result += int(sys.argv[i])
    print(result)
