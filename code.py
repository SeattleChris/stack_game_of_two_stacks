#!/bin/python3

import os

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    idx, pos = len(a), len(b)
    total_a, total_b = sum(a), sum(b)
    while maxSum < total_a:
        idx -= 1
        total_a -= a[idx]
    while maxSum < total_b:
        pos -= 1
        total_b -= b[pos]
    if idx < pos:
        a, b = b, a
        idx, pos = pos, idx
    best, end, pos = idx, pos, 0
    extra = maxSum - sum(a[:idx])
    while idx > -1 and pos < end:
        while pos < end and extra >= (tmp := b[pos]):
            extra -= tmp
            pos += 1
        if best < (score := idx + pos):
            best = score
        idx -= 1
        extra += a[idx]
    return best


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g = int(input().strip())
    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        maxSum = int(first_multiple_input[2])
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        result = twoStacks(maxSum, a, b)
        fptr.write(str(result) + '\n')
    fptr.close()
