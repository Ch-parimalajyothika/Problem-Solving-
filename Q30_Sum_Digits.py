def sum_digits(n):
    n = abs(n)
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

n = int(input("Enter a number: "))
print("Sum of digits =", sum_digits(n))
