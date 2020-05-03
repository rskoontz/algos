#!/usr/bin/env python3

#example of a logarithmic Time -- O(log n)
#this will reduce the size of the input(n) in each step
#to help compute the search more efficiently

def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if value < data[mid]:
            right = mid - 1
        elif value > data[mid]:
            left = mid + 1
        else:
            return mid
    raise ValueError('Value is not found in the list')

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(data, 10))