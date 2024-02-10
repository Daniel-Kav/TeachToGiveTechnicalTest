#Write a program that takes an integer as input and returns an integer with reversed digit
#ordering.

def reverse(num):
    if num < 0:
        return int(str(num)[::-1][-1] + str(num)[::-1][:-1])
    elif num == 0:
        return num
    else:
        return int(str(num)[::-1])

print(reverse(65))