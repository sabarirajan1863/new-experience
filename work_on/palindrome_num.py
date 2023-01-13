def palindrome_num(i):
    while str(i) != str(i)[::-1]:
        i -= 1
    return i
print(palindrome_num(1000)) 
print(palindrome_num(22000))
print(palindrome_num(200))
