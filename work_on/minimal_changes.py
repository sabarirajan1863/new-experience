def minimal_changes(string):
    target = string[0]
    return len(string) - string.count(target)
print(minimal_changes("ABCDA"))
print(minimal_changes("BBBX"))