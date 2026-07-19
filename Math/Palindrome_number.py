def is_palindrome(x):

    x = str(x)

    return x == x[::-1]


print(is_palindrome(121))
print(is_palindrome(123))