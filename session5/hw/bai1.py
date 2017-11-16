numbers = [1, 6, 8, 1, 2, 1, 5, 6]

a = int(input("enter a number: "))
numbers_count = 0

for i in numbers:
    if i == a:
        numbers_count += 1

print("{0} apper {1} times in my list".format(a, numbers_count))
