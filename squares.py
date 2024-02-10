#Write a program that takes an integer as input and returns true if the input is a power of two.

def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0

print(is_power_of_two(16))