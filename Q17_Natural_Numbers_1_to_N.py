def natural_numbers(n):
    result = []
    i = 1
    while i <= n:
        result.append(i)
        i += 1
    return result

n = int(input("Enter n: "))
print(*natural_numbers(n))
