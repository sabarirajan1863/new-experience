string = input("Enter a string: ")
reversed_string = ""
for i in string:
    reversed_string = i + reversed_string
print("Reversed string:", reversed_string)
if string == reversed_string:
    print("The string is palindrome")
else:
    print("The string is not a palindrome")
