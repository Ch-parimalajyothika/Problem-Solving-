def odd_numbers():
    result = []
    i = 1
    while i <= 100:
        result.append(i)
        i += 2
    return result

print(*odd_numbers())
