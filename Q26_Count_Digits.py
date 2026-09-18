def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n:
        count += 1
        n //= 10
    return count

n = int(input("Enter a number: "))
print("Number of digits =", count_digits(n))
