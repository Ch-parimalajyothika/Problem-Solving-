def is_palindrome(n):
    original = abs(n)
    temp = original
    reverse = 0
    while temp:
        reverse = reverse * 10 + temp % 10
        temp //= 10
    return reverse == original

n = int(input("Enter a number: "))
print("Palindrome" if is_palindrome(n) else "Not a Palindrome")
