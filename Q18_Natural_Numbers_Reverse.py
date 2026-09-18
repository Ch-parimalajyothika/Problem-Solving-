def reverse_natural_numbers(n):
    result = []
    while n >= 1:
        result.append(n)
        n -= 1
    return result

n = int(input("Enter n: "))
print(*reverse_natural_numbers(n))
