import math

T = int(input())
# loop through each test case
for t in range(T):
    N = int(input())
    # store integers separated by a space as a list
    A = [int(x) for x in input().split()]
    half = math.ceil(len(A) / 2)
    # first element must be 1 and middle must contain 7, not RA and continue to next test case
    if A[0] != 1 or A[half - 1] != 7:
        print('no')
        continue
    for i in range(half):
        # opposite elements must be equal and element must be same or one more than the previous
        if not (A[i] == A[len(A)-i-1] and (A[i] == A[i-1] or A[i] == A[i-1] + 1)):
            print('no')
            break
        if i == half - 1:
            print('yes')
