# python_loops_notes.py
# Minimal, practical reference for Python loops: for, while, range, enumerate, zip, dict loops,
# loop control (break/continue/else), comprehensions, nested loops, and idioms. [web:11][web:10]

# ----------------------------
# for loops over iterables
# ----------------------------
nums = [1, 2, 3]
for n in nums:
    print(n)  # prints 1 2 3 on separate lines [web:10]

# iterate string
for ch in "abc":
    print(ch)  # 'a', 'b', 'c' [web:10]

# unpacking in loop
pairs = [(1, "a"), (2, "b")]
for i, s in pairs:
    print(i, s)  # 1 a / 2 b [web:10]

# ----------------------------
# range usage
# ----------------------------
for i in range(5):       # 0..4
    pass                 # placeholder [web:15]
for i in range(2, 10, 2):  # 2,4,6,8
    print(i)             # even numbers under 10 [web:15]

# ----------------------------
# enumerate: index + value
# ----------------------------
colors = ["red", "green", "blue"]
for idx, c in enumerate(colors, start=1):
    print(idx, c)  # 1 red, 2 green, 3 blue [web:16]

# ----------------------------
# zip: parallel iteration
# ----------------------------
names = ["Ada", "Linus", "Guido"]
langs = ["Python", "C", "Python"]
for name, lang in zip(names, langs):
    print(f"{name} -> {lang}")  # pairs aligned by position [web:10]

# ----------------------------
# dict iteration
# ----------------------------
cap = {"IN": "Delhi", "US": "DC"}
for k in cap:                # keys by default
    print(k, cap[k])         # IN Delhi / US DC [web:16]
for k, v in cap.items():     # key, value
    print(k, v)              # idiomatic for dicts [web:16]

# ----------------------------
# while loops
# ----------------------------
count = 3
while count > 0:
    print(count)
    count -= 1               # 3 2 1 [web:15]

# ----------------------------
# loop control: break, continue, else
# ----------------------------
# break: exit loop early
for n in [1, 3, 5, 7]:
    if n == 5:
        print("found 5, break")
        break                # stops after 5 [web:10]
# continue: skip to next iteration
for n in [1, -2, 3, -4]:
    if n < 0:
        continue
    print(n)                 # prints only positives: 1, 3 [web:11]
# else on loops: runs only if loop wasn’t broken
target = 42
data = [10, 20, 30]
for x in data:
    if x == target:
        print("hit")
        break
else:
    print("not found")       # prints because no break occurred [web:10]

# ----------------------------
# nested loops
# ----------------------------
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for val in row:
        print(val)           # 1 2 3 4 [web:10]

# ----------------------------
# list comprehensions (compact loops)
# ----------------------------
squares = [x * x for x in range(5)]                # [0,1,4,9,16] [web:11]
evens_sq = [x * x for x in range(10) if x % 2 == 0]  # filter + transform [web:11]

# dict/set comprehensions
square_map = {x: x * x for x in range(3)}          # {0:0,1:1,2:4} [web:10]
unique_first_letters = {name[0] for name in names}  # {'A','L','G'} [web:10]

# ----------------------------
# advanced iteration tips
# ----------------------------
# reversed iteration
for c in reversed(colors):
    print(c)  # blue, green, red [web:16]

# sorted iteration (non-destructive)
for n in sorted([3, 1, 2]):
    print(n)  # 1 2 3 [web:10]

# iterate multiple sequences of unequal length safely
from itertools import zip_longest
a, b = [1, 2], [10, 20, 30]
for x, y in zip_longest(a, b, fillvalue=None):
    print(x, y)  # pairs with fill for missing items [web:10]

# flatten one level using itertools.chain (avoids nested loop)
from itertools import chain
for v in chain(*matrix):
    print(v)  # 1 2 3 4 [web:10]

# ----------------------------
# common patterns
# ----------------------------
# sentinel-controlled while
line = "data"
while line:
    # process line...
    line = ""  # simulate end [web:15]

# accumulating in loop
total = 0
for n in range(1, 6):
    total += n
print(total)  # 15 [web:10]

# for-else: check prime (simple demo)
n = 11
for d in range(2, int(n**0.5) + 1):
    if n % d == 0:
        print("composite")
        break
else:
    print("prime")  # prints 'prime' for 11 [web:10]

# ----------------------------
# pitfalls & notes
# ----------------------------
# - Don’t mutate a list while iterating; iterate over a copy (list(items)) or build a new list. [web:10]
# - Use enumerate instead of manual index counters. [web:16]
# - Prefer for-loops over range(len(seq)) unless indexes are required. [web:10]
# - Use comprehensions for simple map/filter; fall back to loops for clarity when complex. [web:11]
# - Use break/continue judiciously; pair with loop-else for "not found" cases. [web:10]
