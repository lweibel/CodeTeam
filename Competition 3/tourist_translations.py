# taking input (on one line separated by a space)
T, M = input().split()
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
DICTIONARY = {"_": " "}

# map each letter in alphabet (upper and lowercase) to the given permutation
for idx, letter in enumerate(ALPHABET):
    DICTIONARY[letter] = M[idx]
    DICTIONARY[letter.upper()] = M[idx].upper()

# loop through each test case
for t in range(int(T)):
    original_str = input()
    decoded_str = ""
    """
    loop through each character in the original string, if the key exists in
    the dictionary, add the value to the decoded string, otherwise just add the
    character from the original string (for '.' ',' '?' '!' characters)
    """
    for letter in original_str:
        if letter in DICTIONARY:
            decoded_str += DICTIONARY[letter]
        else:
            decoded_str += letter
    print(decoded_str)
