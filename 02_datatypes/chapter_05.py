# Lists are mutable, ordered sequences in Python.
# They are defined using square brackets [].
# Use lists when you need a collection that can be modified after creation.
# Lists can store elements of different types and allow duplicates.

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print("Empty:", empty_list)
print("Numbers:", numbers)
print("Mixed:", mixed)
print("Nested:", nested)

# Indexing and slicing (same as tuples/strings)
print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])
print("Slice with step [::2]:", numbers[::2])

# Membership test using 'in' and 'not in'
print(f"\n3 in numbers: {3 in numbers}")
print(f"10 in numbers: {10 in numbers}")
print(f"'hello' not in mixed: {'hello' not in mixed}")

# List methods — appending and extending
fruits = ["apple", "banana"]
print(f"\nOriginal: {fruits}")
fruits.append("cherry")  # adds single element
print(f"After append: {fruits}")
fruits.extend(["date", "elderberry"])  # adds multiple elements
print(f"After extend: {fruits}")

# Insert at specific index
fruits.insert(1, "apricot")
print(f"After insert at index 1: {fruits}")

# Remove elements
fruits.remove("apricot")  # removes first occurrence of value
print(f"After remove('apricot'): {fruits}")

popped = fruits.pop()  # removes and returns last element
print(f"After pop(): {fruits}, popped: {popped}")

popped_index = fruits.pop(1)  # removes and returns element at index
print(f"After pop(1): {fruits}, popped: {popped_index}")

# Clear entire list
temp = [1, 2, 3]
temp.clear()
print(f"\nAfter clear(): {temp}")

# Finding index and counting
data = [10, 20, 30, 20, 40, 20]
print(f"\nData: {data}")
print(f"Index of 30: {data.index(30)}")
print(f"Count of 20: {data.count(20)}")

# Sorting
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nUnsorted: {unsorted}")
unsorted.sort()
print(f"After sort(): {unsorted}")
unsorted.sort(reverse=True)
print(f"After sort(reverse=True): {unsorted}")

# Reversing
reversed_list = [1, 2, 3, 4, 5]
print(f"\nOriginal: {reversed_list}")
reversed_list.reverse()
print(f"After reverse(): {reversed_list}")

# Copying lists (shallow copy)
original = [1, 2, 3]
shallow_copy = original.copy()
shallow_copy[0] = 99
print(f"\nOriginal: {original}")
print(f"Shallow copy after change: {shallow_copy}")

# List comprehension — create new list with transformation
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")

evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens 0-9: {evens}")

# Nested list operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatrix: {matrix}")
print(f"matrix[1][2]: {matrix[1][2]}")
matrix[0].append(10)
print(f"After appending to first row: {matrix}")

# List mutability demo
my_list = [1, 2, 3, 4, 5]
print(f"\nOriginal: {my_list}")
my_list[2] = 99  # can modify (unlike tuples)
print(f"After modification: {my_list}")

# Length and iteration
print(f"\nLength: {len(my_list)}")
print("Iteration:")
for item in my_list:
    print(f"  {item}")

# Enumerate — get index and value
print("\nWith enumerate:")
for index, value in enumerate(my_list):
    print(f"  Index {index}: {value}")

# Combining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"\nCombined: {combined}")

repeated = [0] * 4
print(f"Repeated: {repeated}")