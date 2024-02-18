#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sums = []
    for i in range(len(arr)):
        arr_copied = arr.copy()
        arr_copied.pop(i)
        sums.append(sum(arr_copied))
    print(min(sums), max(sums))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
