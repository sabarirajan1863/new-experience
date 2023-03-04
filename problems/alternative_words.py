string = input()
reverse_str = ""
for i in string:
    reverse_str = i + reverse_str
alternative_words = ""
for i in range(len(reverse_str)):
    if i % 2 == 0:
        alternative_words += reverse_str[i].upper()
    else:
        alternative_words += reverse_str[i]
print(alternative_words)
