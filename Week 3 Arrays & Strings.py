
from collections import Counter

# Q1. Two Sum
def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i

    return []


# Q2. Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Q3. Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


# Q4. Kadane's Algorithm
def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Q5. Anagram (Frequency Count)
def is_anagram(s, t):
    return Counter(s) == Counter(t)


# Q6. Rotate Array by K Steps
def rotate(nums, k):
    n = len(nums)
    k %= n

    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums


# Q7. Best Time to Buy and Sell Stock
def max_profit(prices):
    min_price = float('inf')
    profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


# Q8. Valid Parentheses
def is_valid(s):
    stack = []
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack.pop() != mapping[char]:
                return False

    return len(stack) == 0



print("Q1. Two Sum")
print(two_sum([2, 7, 11, 15], 9))

print("\nQ2. Longest Substring Without Repeating Characters")
print(length_of_longest_substring("abcabcbb"))

print("\nQ3. Remove Duplicates")
arr = [1, 1, 2, 2, 3, 4, 4]
new_length = remove_duplicates(arr)
print("New Length:", new_length)
print("Updated Array:", arr[:new_length])

print("\nQ4. Maximum Subarray Sum")
print(max_subarray([1, -2, 3, 4, -1, 2, 1, -5, 4]))

print("\nQ5. Anagram")
print(is_anagram("listen", "silent"))

print("\nQ6. Rotate Array")
print(rotate([1, 2, 3, 4, 5], 2))

print("\nQ7. Best Time to Buy and Sell Stock")
print(max_profit([7, 1, 5, 3, 6, 4]))

print("\nQ8. Valid Parentheses")
print(is_valid("([])"))
print(is_valid("([)]"))

