from collections import defaultdict, Counter

# Q1. Hash Table Implementation

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]

    def hash_function(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))
        self.size += 1

        if self.size / self.capacity > 0.75:
            self.resize()

    def get(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.size -= 1
                return True
        return False

    def resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)


# Q2. Hash Collision Explanation

collision_explanation = """
Hash Collision:
A collision occurs when two different keys produce the same hash index.

Separate Chaining:
- Stores multiple key-value pairs in a bucket (list).
- Easy insertion and deletion.
- Average Time: O(1)

Open Addressing (Linear Probing):
- Searches for the next available slot.
- Better cache locality.
- Suffers from clustering.

Python dict:
- Uses Open Addressing with an optimized probing algorithm.
"""

# Q3. Group Anagrams

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())

# Q4. Longest Consecutive Sequence

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


# Q5. Top K Frequent Elements (Bucket Sort)

def top_k_frequent(nums, k):
    frequency = Counter(nums)

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in frequency.items():
        buckets[count].append(num)

    result = []

    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)

            if len(result) == k:
                return result

    return result


# Q6. Find Unique Pairs with Target Sum

def find_pairs(nums, target):
    seen = set()
    result = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            result.add(tuple(sorted((num, complement))))

        seen.add(num)

    return list(result)


# Q7. LRU Cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Q8. Valid Sudoku

def is_valid_sudoku(board):

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):

            value = board[r][c]

            if value == '.':
                continue

            box = (r // 3) * 3 + (c // 3)

            if value in rows[r]:
                return False

            if value in cols[c]:
                return False

            if value in boxes[box]:
                return False

            rows[r].add(value)
            cols[c].add(value)
            boxes[box].add(value)

    return True


if __name__ == "__main__":

    print("=" * 60)
    print("Q1. Hash Table")
    print("=" * 60)

    ht = HashTable()

    for i in range(25):
        ht.put(f"key{i}", i)

    print("key10 =", ht.get("key10"))
    print("key24 =", ht.get("key24"))

    ht.delete("key10")
    print("After delete:", ht.get("key10"))

    print("\n" + "=" * 60)
    print("Q2. Hash Collision")
    print("=" * 60)
    print(collision_explanation)

    print("\n" + "=" * 60)
    print("Q3. Group Anagrams")
    print("=" * 60)

    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(group_anagrams(words))

    print("\n" + "=" * 60)
    print("Q4. Longest Consecutive Sequence")
    print("=" * 60)

    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive(nums))

    print("\n" + "=" * 60)
    print("Q5. Top K Frequent Elements")
    print("=" * 60)

    nums = [1, 1, 1, 2, 2, 3]
    print(top_k_frequent(nums, 2))

    print("\n" + "=" * 60)
    print("Q6. Unique Pairs")
    print("=" * 60)

    nums = [1, 2, 3, 4, 3, 2, 5, 0]
    print(find_pairs(nums, 5))

    print("\n" + "=" * 60)
    print("Q7. LRU Cache")
    print("=" * 60)

    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    print(cache.get(1))

    cache.put(3, 3)

    print(cache.get(2))

    print("\n" + "=" * 60)
    print("Q8. Valid Sudoku")
    print("=" * 60)

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print(is_valid_sudoku(board))

