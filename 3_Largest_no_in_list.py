def find_largest(numbers):
    largest = numbers[0]          # assume first number is largest
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example
my_list = [4, 9, 2, 7, 15, 3]
print(find_largest(my_list))
