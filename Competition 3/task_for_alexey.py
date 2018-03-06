def lcm(a, b):
    # finds the least common multiple
    return a*b // gcd(a, b)

def gcd(a, b):
    # finds the greatest common divisor
    if a == 0: return b
    return gcd(b % a, a)

T = int(input())
# loop through each test case
for t in range(T):
    N = int(input())
    # store integers separated by a space as a list, sort for early break
    A = sorted([int(x) for x in input().split()])
    # just need to find lowest common multiple of all pairwise elements
    lowest_freeze_time = lcm(A[0], A[1])
    for i, a in enumerate(A):
        for b in A[i+1:]:
            freeze_time = lcm(a, b)
            if freeze_time < lowest_freeze_time:
                lowest_freeze_time = freeze_time
            """
            this means the lowest freeze time is less than the number you are looking at, and since the
            array is sorted, you can break out of the loop because it is not possible to find a lower
            freeze time.
            """
            if lowest_freeze_time <= b:
                break
    print(lowest_freeze_time)
