# Tuples are immutable, ordered sequences in Python.
# They are defined using parentheses () or just commas.
# Use tuples when data should not be modified after creation.
# They're also lowkey more memory-efficient than lists, so if you don't need mutability, 
# tuples are the move.

# Creating tuples
empty_tuple = ()
single_item = (42,)  # trailing comma required for single-element tuple
coordinates = (10, 20, 30)
mixed = ("hello", 3.14, True, [1, 2])  # can hold different types
without_parens = 1, 2, 3  # packing — parentheses are optional

print("Empty:", empty_tuple)
print("Single:", single_item)
print("Coordinates:", coordinates)
print("Mixed:", mixed)
print("Without parens:", without_parens)

# Indexing and slicing (same as lists/strings)
print("\nFirst:", coordinates[0])
print("Last:", coordinates[-1])
print("Slice:", mixed[1:3])

# Unpacking
x, y, z = coordinates
print(f"\nUnpacked: x={x}, y={y}, z={z}")

# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print(f"First: {first}, Rest: {rest}")

# Tuple methods (only two, since tuples are immutable)
nums = (1, 3, 7, 3, 9, 3, 2)
print(f"\nCount of 3: {nums.count(3)}")
print(f"Index of 7: {nums.index(7)}")

# Nested tuples
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"\nMatrix[1][2]: {matrix[1][2]}")

# Tuple as dictionary key (possible because tuples are hashable)
locations = {(28.6, 77.2): "Delhi", (51.5, -0.1): "London"}
print(f"\nLocation lookup: {locations[(51.5, -0.1)]}")

# Immutability demo
try:
    coordinates[0] = 99
except TypeError as e:
    print(f"\nCannot modify tuple: {e}")

# Concatenation and repetition (creates new tuples)
combined = (1, 2) + (3, 4)
repeated = ("ha",) * 3
print(f"\nCombined: {combined}")
print(f"Repeated: {repeated}")

# Tuple vs list — tuples are faster and use less memory
import sys
list_size = sys.getsizeof([1, 2, 3, 4, 5])
tuple_size = sys.getsizeof((1, 2, 3, 4, 5))
print(f"\nList size: {list_size} bytes")
print(f"Tuple size: {tuple_size} bytes")

# Common use case: returning multiple values from a function
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([4, 1, 8, 2, 9])
print(f"\nMin: {lo}, Max: {hi}")

# Named tuples for readable structured data
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print(f"\nNamedTuple: {p}")
print(f"Access by name: x={p.x}, y={p.y}")