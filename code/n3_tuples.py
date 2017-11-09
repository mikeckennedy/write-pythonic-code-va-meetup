# create a tuple
m = .4,
print(type(m), m)
m = .4, .9, 4, 18.9
print(type(m), m)

# unpack a tuple
x, y, _, _ = m
x, y = y, x
print(x, y)

# These numbers look familiar...
n = [1, 1, 2, 3, 5, 8, 12, 21]
for idx, f in enumerate(n):
    print(f" {idx+1}. {f}")


# Show the ith Fibonacci number

# example: fibonacci generator with simple(est?) algorithm
def fib(limit):
    nums = []
    current, nxt = 0, 1
    while len(nums) < limit:
        current, nxt = nxt, current + nxt
        nums.append(current)

    return nums


print(fib(10))
