# ============================================================
#   Python List Functions — DSA Cheat Sheet
# ============================================================

# ─────────────────────────────────────────────────────────────
# 1. CREATION & BASIC SETUP
# ─────────────────────────────────────────────────────────────

arr = [5, 2, 8, 1, 9, 3]
empty = []
zeros = [0] * 5          # [0, 0, 0, 0, 0]  — pre-sized array
matrix = [[0]*3 for _ in range(3)]  # 2D list (3x3)

print("=" * 55)
print("1. CREATION")
print("=" * 55)
print(f"arr     : {arr}")
print(f"zeros   : {zeros}")
print(f"matrix  : {matrix}")


# ─────────────────────────────────────────────────────────────
# 2. APPEND / INSERT / EXTEND  — O(1) / O(n) / O(k)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("2. APPEND / INSERT / EXTEND")
print("=" * 55)

a = [1, 2, 3]
a.append(4)           # add to end         → [1,2,3,4]
print(f"append(4)      : {a}")

a.insert(1, 99)       # insert at index 1  → [1,99,2,3,4]
print(f"insert(1,99)   : {a}")

a.extend([10, 11])    # merge another list  → [1,99,2,3,4,10,11]
print(f"extend([10,11]): {a}")


# ─────────────────────────────────────────────────────────────
# 3. REMOVE / POP / CLEAR  — O(n) / O(1) amortized / O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("3. REMOVE / POP / CLEAR")
print("=" * 55)

b = [1, 2, 3, 4, 5]
popped = b.pop()       # remove & return last element
print(f"pop()      → {popped}, list: {b}")

popped_i = b.pop(1)    # remove & return index 1
print(f"pop(1)     → {popped_i}, list: {b}")

b.remove(3)            # remove first occurrence of value 3
print(f"remove(3)  : {b}")

c = [1, 2, 3]
c.clear()              # empty the list
print(f"clear()    : {c}")


# ─────────────────────────────────────────────────────────────
# 4. SEARCH — O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("4. SEARCH  (index / in / count)")
print("=" * 55)

d = [10, 20, 30, 20, 50]
print(f"list               : {d}")
print(f"index(20)          : {d.index(20)}")     # first occurrence
print(f"20 in d            : {20 in d}")         # membership O(n)
print(f"count(20)          : {d.count(20)}")     # frequency


# ─────────────────────────────────────────────────────────────
# 5. SORT & REVERSE  — O(n log n) / O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("5. SORT & REVERSE")
print("=" * 55)

e = [5, 2, 8, 1, 9]
e.sort()                        # ascending in-place
print(f"sort() asc         : {e}")

e.sort(reverse=True)            # descending in-place
print(f"sort(reverse=True) : {e}")

f = [3, 1, 4, 1, 5]
g = sorted(f)                   # returns NEW sorted list
print(f"sorted()  new list : {g}  original: {f}")

e.reverse()                     # reverse in-place O(n)
print(f"reverse()          : {e}")

# sort by key — useful in graph problems (e.g. sort edges by weight)
pairs = [(1, 5), (3, 2), (2, 8)]
pairs.sort(key=lambda x: x[1])
print(f"sort by 2nd elem   : {pairs}")


# ─────────────────────────────────────────────────────────────
# 6. SLICING  — O(k)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("6. SLICING  arr[start:stop:step]")
print("=" * 55)

h = [0, 1, 2, 3, 4, 5, 6]
print(f"original           : {h}")
print(f"h[2:5]             : {h[2:5]}")     # [2,3,4]
print(f"h[:3]              : {h[:3]}")      # [0,1,2]
print(f"h[4:]              : {h[4:]}")      # [4,5,6]
print(f"h[::2]             : {h[::2]}")     # every 2nd
print(f"h[::-1]            : {h[::-1]}")    # reversed copy


# ─────────────────────────────────────────────────────────────
# 7. STACK OPERATIONS  — O(1)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("7. LIST AS STACK  (LIFO)")
print("=" * 55)

stack = []
stack.append(10)     # push
stack.append(20)
stack.append(30)
print(f"stack after pushes : {stack}")
print(f"peek (top)         : {stack[-1]}")
print(f"pop                : {stack.pop()}  → {stack}")


# ─────────────────────────────────────────────────────────────
# 8. QUEUE OPERATIONS via collections.deque  — O(1)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("8. LIST AS QUEUE  (use deque — O(1) both ends)")
print("=" * 55)

from collections import deque
queue = deque()
queue.append(1)       # enqueue right
queue.append(2)
queue.append(3)
print(f"queue              : {list(queue)}")
print(f"dequeue (popleft)  : {queue.popleft()}  → {list(queue)}")
queue.appendleft(0)   # enqueue left
print(f"appendleft(0)      : {list(queue)}")


# ─────────────────────────────────────────────────────────────
# 9. MIN / MAX / SUM / LEN  — O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("9. AGGREGATE FUNCTIONS")
print("=" * 55)

nums = [3, 7, 1, 9, 4]
print(f"list    : {nums}")
print(f"min()   : {min(nums)}")
print(f"max()   : {max(nums)}")
print(f"sum()   : {sum(nums)}")
print(f"len()   : {len(nums)}")


# ─────────────────────────────────────────────────────────────
# 10. COPY  — O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("10. COPY  (shallow vs deep)")
print("=" * 55)

original = [1, 2, 3]
shallow  = original.copy()      # or original[:]
shallow.append(99)
print(f"original after shallow copy mutation : {original}")  # unchanged

import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0].append(99)
print(f"original after deep copy mutation   : {nested}")     # unchanged


# ─────────────────────────────────────────────────────────────
# 11. LIST COMPREHENSION  — O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("11. LIST COMPREHENSION")
print("=" * 55)

squares   = [x**2 for x in range(6)]
evens     = [x for x in range(10) if x % 2 == 0]
flat      = [x for row in [[1,2],[3,4],[5,6]] for x in row]
print(f"squares            : {squares}")
print(f"evens 0-9          : {evens}")
print(f"flatten 2D         : {flat}")


# ─────────────────────────────────────────────────────────────
# 12. ENUMERATE & ZIP  — O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("12. ENUMERATE & ZIP")
print("=" * 55)

fruits = ["apple", "banana", "cherry"]
for i, val in enumerate(fruits, start=1):
    print(f"  enumerate: index {i} → {val}")

keys   = ["a", "b", "c"]
values = [10,  20,  30]
zipped = list(zip(keys, values))
print(f"zip result         : {zipped}")
d_from_zip = dict(zip(keys, values))
print(f"dict from zip      : {d_from_zip}")


# ─────────────────────────────────────────────────────────────
# 13. TWO POINTERS PATTERN  — O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("13. TWO POINTERS  — check if pair sums to target")
print("=" * 55)

def two_sum_sorted(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return (lo, hi)
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return None

sorted_arr = [1, 3, 5, 7, 9, 11]
print(f"array  : {sorted_arr}")
print(f"target 10 → indices: {two_sum_sorted(sorted_arr, 10)}")
print(f"target 20 → indices: {two_sum_sorted(sorted_arr, 20)}")


# ─────────────────────────────────────────────────────────────
# 14. SLIDING WINDOW PATTERN  — O(n)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("14. SLIDING WINDOW  — max sum subarray of size k")
print("=" * 55)

def max_sum_window(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        best = max(best, window_sum)
    return best

w_arr = [2, 1, 5, 1, 3, 2]
print(f"array  : {w_arr}")
print(f"max sum of window k=3 : {max_sum_window(w_arr, 3)}")


# ─────────────────────────────────────────────────────────────
# 15. PREFIX SUM  — O(n) build, O(1) query
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("15. PREFIX SUM  — range sum query")
print("=" * 55)

def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        prefix[i+1] = prefix[i] + v
    return prefix

def range_sum(prefix, l, r):   # sum arr[l..r] inclusive
    return prefix[r+1] - prefix[l]

p_arr   = [1, 2, 3, 4, 5]
prefix  = build_prefix(p_arr)
print(f"array          : {p_arr}")
print(f"prefix         : {prefix}")
print(f"range_sum(1,3) : {range_sum(prefix, 1, 3)}")  # 2+3+4 = 9
print(f"range_sum(0,4) : {range_sum(prefix, 0, 4)}")  # 15


# ─────────────────────────────────────────────────────────────
# COMPLEXITY SUMMARY
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("COMPLEXITY SUMMARY")
print("=" * 55)
summary = [
    ("append(x)",          "O(1) amortized"),
    ("pop()  [end]",       "O(1)"),
    ("pop(i) [middle]",    "O(n)"),
    ("insert(i, x)",       "O(n)"),
    ("remove(x)",          "O(n)"),
    ("index(x)",           "O(n)"),
    ("x in list",          "O(n)"),
    ("sort()",             "O(n log n)"),
    ("reverse()",          "O(n)"),
    ("len()",              "O(1)"),
    ("slicing [i:j]",      "O(k)"),
    ("copy()",             "O(n)"),
    ("deque.appendleft()", "O(1)"),
    ("deque.popleft()",    "O(1)"),
]
for op, cplx in summary:
    print(f"  {op:<25} {cplx}")

print("\nDone.")