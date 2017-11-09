# create a fib generator
def fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


def odds(nums):
    for n in nums:
        if n % 2 == 1:
            yield n


nums = fib()
odd_nums = odds(nums)
print(type(odd_nums))

for o in odd_nums:
    print(o)
    if o > 100:
        break
print("Next loop")
for o in odd_nums:
    print(f"More: {o}")
    if o > 200:
        break

