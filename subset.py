def sort_and_check_sum(numbers, d):
    sorted_numbers = sorted(numbers)
    total_sum = sum(sorted_numbers)
    return sorted_numbers, total_sum == d

n = int(input("Enter number of elements: "))
numbers = []

for _ in range(n):
    numbers.append(int(input("Enter number: ")))

d = int(input("Enter value of d: "))

sorted_numbers, is_equal = sort_and_check_sum(numbers, d)

print(sorted_numbers)
print("Equal" if is_equal else "Not Equal")