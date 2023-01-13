def max_product(numbers):
    numbers.sort(reverse=True)
    max_product = numbers[0] * numbers[1]
    return max_product

print(max_product([1, 2, 3, 4, 5, 6, 7])) 
print(max_product([10, 100, 20, 40, 102, 22])) 