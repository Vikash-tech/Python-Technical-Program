
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Q1 Append
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
 
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = None
        curr = self.head

        while curr and curr.data != value:
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next

    def search(self, value):
        curr = self.head

        while curr:
            if curr.data == value:
                return True
            curr = curr.next

        return False
    
    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next

        print("None")


# ==========================
# Q2 Reverse Linked List
# ==========================
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


# ==========================
# Q3 Floyd Cycle Detection
# ==========================
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# ==========================
# Q4 Merge Two Sorted Lists
# ==========================
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    tail.next = l1 if l1 else l2

    return dummy.next


# ==========================
# Q5 Remove Nth Node From End
# ==========================
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


# ==========================
# Q7 Find Cycle Start
# ==========================
def detect_cycle_start(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# ==========================
# Q8 Palindrome Linked List
# ==========================
def is_palindrome(head):
    if not head or not head.next:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    left = head
    right = prev

    while right:
        if left.data != right.data:
            return False

        left = left.next
        right = right.next

    return True


# ==========================
# Helper Function
# ==========================
def print_head(head):
    curr = head

    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next

    print("None")


if __name__ == "__main__":

    print("\n===== Q1 LinkedList Operations =====")
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.print_list()

    ll.prepend(5)
    ll.print_list()

    print("Search 20:", ll.search(20))
    print("Search 100:", ll.search(100))

    ll.delete_by_value(20)
    ll.print_list()

    print("\n===== Q2 Reverse Linked List =====")
    rev = LinkedList()

    for x in [1, 2, 3, 4]:
        rev.append(x)

    print("Original:")
    rev.print_list()

    rev.head = reverse_list(rev.head)

    print("Reversed:")
    rev.print_list()

    print("\n===== Q3 Floyd Cycle Detection =====")
    cycle_head = Node(1)
    cycle_head.next = Node(2)
    cycle_head.next.next = Node(3)
    cycle_head.next.next.next = Node(4)

    cycle_head.next.next.next.next = cycle_head.next

    print("Cycle Exists:", has_cycle(cycle_head))

    print("\n===== Q4 Merge Sorted Lists =====")

    a1 = Node(1)
    a1.next = Node(3)
    a1.next.next = Node(5)

    a2 = Node(2)
    a2.next = Node(4)
    a2.next.next = Node(6)

    merged = merge_sorted_lists(a1, a2)

    print("Merged List:")
    print_head(merged)

    print("\n===== Q5 Remove 2nd Node From End =====")

    r = LinkedList()

    for x in [1, 2, 3, 4, 5]:
        r.append(x)

    print("Before:")
    r.print_list()

    r.head = remove_nth_from_end(r.head, 2)

    print("After:")
    r.print_list()

    print("\n===== Q7 Detect Cycle Start =====")

    c1 = Node(1)
    c2 = Node(2)
    c3 = Node(3)
    c4 = Node(4)
    c5 = Node(5)

    c1.next = c2
    c2.next = c3
    c3.next = c4
    c4.next = c5
    c5.next = c3

    start = detect_cycle_start(c1)

    if start:
        print("Cycle starts at node:", start.data)
    else:
        print("No cycle")

    print("\n===== Q8 Palindrome Linked List =====")

    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(3)
    p4 = Node(2)
    p5 = Node(1)

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5

    print("Is Palindrome:", is_palindrome(p1))