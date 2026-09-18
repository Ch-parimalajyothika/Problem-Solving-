def even_numbers():
    result = []
    i = 2
    while i <= 100:
        result.append(i)
        i += 2
    return result

print(*even_numbers())
