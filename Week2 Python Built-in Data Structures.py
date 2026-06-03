#Week 2: Python Built-in Data Structures


#----------------------------------------------------------------------------------------------------

# Q1. When would you use a set instead of a list?

# Use a set when:

# You need unique elements.
# You need fast membership testing (in operation).
# Order is not important.

# Examples:

# Tracking visited URLs in a web crawler.
# Checking banned usernames during registration.

# Complexity:

# List lookup: O(n)
# Set lookup: O(1) average

#----------------------------------------------------------------------------------------------------

# Q2. What is the time complexity of checking if an element exists?

# Structure	Complexity
# List	O(n)
# Set	O(1) average
# Dictionary	O(1) average

# Reason:
# Lists scan elements sequentially.
# Sets and dictionaries use hash tables to locate elements directly.

#----------------------------------------------------------------------------------------------------


# Q3. Find the most common character using Counter
from collections import Counter

def most_common_character(s):
    if not s:
        return None

    char, count = Counter(s).most_common(1)[0]
    return char, count

print(most_common_character("mississippi"))
# ('s', 4)

Complexity: O(n)

#----------------------------------------------------------------------------------------------------

# Q4. Find IDs present in both lists
def common_ids(list1, list2):
    return list(set(list1) & set(list2))

admins = [101, 202, 303]
active = [202, 303, 404]

print(common_ids(admins, active))
# # [202, 303]

# Most Efficient Approach: Set Intersection

Complexity: O(n + m)

#----------------------------------------------------------------------------------------------------

# Q5. Why is deque preferred over list for a queue?
#Operation	List	Deque
#Append Right	O(1)	O(1)
#Remove Left	O(n)	O(1)
from collections import deque

queue = deque()
queue.append("A")
queue.append("B")

print(queue.popleft())  
# Reason: list.pop(0) shifts all elements, while deque.popleft() is constant time.

#----------------------------------------------------------------------------------------------------

# Q6. Group words by first letter using defaultdict
from collections import defaultdict
def group_by_first_letter(words):
    groups = defaultdict(list)

    for word in words:
        groups[word[0]].append(word)

    return dict(groups)

words = ["apple", "avocado", "banana"]
print(group_by_first_letter(words))

# # {'a': ['apple', 'avocado'], 'b': ['banana']}

# Benefit: No need to check if a key already exists.

#----------------------------------------------------------------------------------------------------

# Q7. What happens if you use a list as a dictionary key?
#   my_dict = {}
#   my_dict[[1, 2, 3]] = "value"

# Output:

# TypeError: unhashable type: 'list'

# Reason:
# Dictionary keys must be hashable and immutable. Lists are mutable, so Python does not allow them as keys.

# Use a tuple instead:

# my_dict[(1, 2, 3)] = "value"

#----------------------------------------------------------------------------------------------------

# Q8. Remove duplicates while preserving order
def remove_duplicates(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# print(remove_duplicates([3,1,4,1,5,9,2,6,5,3]))
# # [3,1,4,5,9,2,6]

# Complexity: O(n)
# Alternative:
# list(dict.fromkeys(items))
