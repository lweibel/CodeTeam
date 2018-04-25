a, b = [int(x) for x in input().split()]

# convert the correct answer to a string
correct_answer = str(a - b)
# increment the last digit by one, if 9 go to 1
last_digit = (int(correct_answer[-1]) % 9) + 1
# print correct answer with changed last digit
print(correct_answer[:len(correct_answer) - 1] + str(last_digit))
