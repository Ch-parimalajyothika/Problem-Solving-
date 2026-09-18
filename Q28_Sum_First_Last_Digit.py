def sum_first_last(n):
    n = abs(n)
    last = n % 10
    while n >= 10:
        n //= 10
    return n + last

n = int(input("Enter a number: "))
print("Sum of first and last digit =", sum_first_last(n))
