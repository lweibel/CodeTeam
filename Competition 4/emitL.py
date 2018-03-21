T = int(input())
for t in range(T):
    S = input()
    letter_count = {'L': 0, 'T': 0, 'I': 0, 'M': 0, 'E': 0}
    for c in S:
        if c in letter_count:
            letter_count[c] += 1
    # you have to be careful when using just list(letter_count.values()), as the order is not guaranteed
    lc_list = [letter_count['L'], letter_count['T'], letter_count['I'], letter_count['M'], letter_count['E']]
    # would be nice to write lc_list >= [2, 2, 2, 2, 2], but list comparison does not work like this
    print('YES') if all(count >= 2 for count in lc_list) or lc_list == [2, 2, 2, 2, 1] else print('NO')
