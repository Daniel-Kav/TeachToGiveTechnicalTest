#Write a program to generate the Fibonacci sequence up to 100.

def fibonacci(limit):
    fibonacci_sequence = [0,1]
    num= 2
    while True:
        next_fibonacci = fibonacci_sequence[num-1] + fibonacci_sequence[num - 2]
        if next_fibonacci <= limit:
            fibonacci_sequence.append(next_fibonacci)
            num += 1
        else:
            break
    return fibonacci_sequence

print(fibonacci(100))