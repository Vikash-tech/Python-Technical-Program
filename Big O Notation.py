# Middle Element (O(1))
def middle_element(lst):
    if not lst:
        return None
    mid = (len(lst) - 1) // 2
    return lst[mid]

print(middle_element([10, 20, 30, 40, 50]))    #Answer - 30
print(middle_element([1, 2, 3, 4]))            #Answer - 2

#------------------------------------------------------------------

#Find Pairs (O(n²))
def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

print(find_pairs([1,2,3,4,5], 5))   #Answer - [(1, 4), (2, 3)]

#-----------------------------------------------------------------------

#Binary Search with Steps (O(log n))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps

arr = list(range(1, 21))
print(binary_search(arr, 14))  #Answer - (13, steps)

#-----------------------------------------------------------------------

# Anagram (O(n), O(1) space)   --- -- contain same Elements
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    counts = [0] * 26

    for i in range(len(s1)):
        counts[ord(s1[i]) - ord('a')] += 1
        counts[ord(s2[i]) - ord('a')] -= 1

    return all(c == 0 for c in counts)

print(is_anagram("listen", "silent"))  # True 
print(is_anagram("hello", "world"))    # False -- Not Contain Same Elements

#-----------------------------------------------------------------------

#Big O

def func_a(n):
    return n * n + 5       # O(1)

def func_b(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i+j+k)   # O(n^3)

def func_c(n):
    while n > 1:
        n = n // 2        # O(log n)

def func_d(n):
    for i in range(n):
        print(i)          # O(n)

def func_e(n):
    if n <= 1:
        return 1
    return func_e(n-1) + func_e(n-1)  # O(2^n)

#-----------------------------------------------------------------------

#Two Sum Optimized (O(n))
def two_sum_fast(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num

        if complement in seen:
            return (seen[complement], i)

        seen[num] = i

    return None

print(two_sum_fast([2,7,11,15], 9))  # (0, 1)

#-----------------------------------------------------------------------

#Merge vs Quick Sort (O(n) space)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([5,2,8,1,9]))

#Time Estimation
import math

n_values = [500, 1000, 10000]

for n in n_values:
    log_time = math.log2(n) * 0.004
    linear_time = n * 0.004
    quadratic_time = (n*n) * 0.004

    print(f"\nn = {n}")
    print(f"O(log n): {log_time:.4f} ms")
    print(f"O(n): {linear_time:.2f} ms")
    print(f"O(n^2): {quadratic_time/1000:.2f} seconds")
