# file = open('hyperskill-dataset-46900908.txt', 'r')
# n = 0
# for line in file:
#     if 'summer' in line:
#         n += 1
#
# print(n)

def check(string):
    if string.isdigit():
        number = int(string)
        minimum = 202
        print(number if number >= minimum else "There are less than 202 apples! You cheated me!")
    else:
        print("It is not a number!")
        