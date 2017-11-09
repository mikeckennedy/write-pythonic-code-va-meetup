# Filter method for even numbers
from typing import List


def find_numbers(nums: List[int], test) -> List[int]:
    other_numbers = []
    for n in nums:
        if test(n):
            other_numbers.append(n)

    return other_numbers

# Sort data

# def is_even(n):
#     return n % 2 == 0
# def is_odd(n):
#     return n % 2 == 1

data = [1, 9, -1, 20, 5, -100, 24]
print(find_numbers(data, lambda n: n % 6 == 0))

result = find_numbers(data, lambda n: n % 6 == 0)

data.sort(key=lambda n: -abs(n))
print(data)
