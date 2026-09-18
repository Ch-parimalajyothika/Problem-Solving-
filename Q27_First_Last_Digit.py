def first_last_digit(n):
    n = abs(n)
    last = n % 10
    while n >= 10:
        n //= 10
    return n, last

n = int(input("Enter a number: "))
first, last = first_last_digit(n)
print("First digit =", first)
print("Last digit =", last)
