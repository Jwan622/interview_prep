"""
Interview Guide - Detecting Cycles in a Linked List: A Dual-Approach Analysis
Introduction & Problem Understanding
Detecting cycles in a linked list is a classic problem that tests a developer's ability to understand and manipulate data structures. In this problem, you are given the head of a singly-linked list. The objective is to determine whether the list contains a cycle. A cycle exists if a node in the list can be visited more than once by following the next pointers continuously.

Key Concepts and Constraints
Node Anatomy:
Each node in the list contains an integer value and a next pointer that points to the subsequent node in the list.

Cycle Detection:
The primary task is to identify whether a cycle exists within the list. If a cycle is detected, the function should return True. Otherwise, it should return False.

Memory Efficiency:
The question poses an implicit challenge: Can you solve it using O(1)O(1)O(1) memory, meaning constant extra space?

Interview Guide - Detecting Cycles in a Linked List: A Dual-Approach Analysis
Introduction & Problem Understanding
Detecting cycles in a linked list is a classic problem that tests a developer's ability to understand and manipulate data structures. In this problem, you are given the head of a singly-linked list. The objective is to determine whether the list contains a cycle. A cycle exists if a node in the list can be visited more than once by following the next pointers continuously.

Key Concepts and Constraints
Node Anatomy:
Each node in the list contains an integer value and a next pointer that points to the subsequent node in the list.

Cycle Detection:
The primary task is to identify whether a cycle exists within the list. If a cycle is detected, the function should return True. Otherwise, it should return False.

Memory Efficiency:
The question poses an implicit challenge: Can you solve it using O(1) memory, meaning constant extra space?


Solution2 is the tortoise and the hair solution:
Intuition and Logic Behind the Solution
Also known as the "hare and tortoise" algorithm, this method uses two pointers that traverse the list at different speeds. The slow pointer moves one step at a time, while the fast pointer moves two steps. If there is a cycle, the fast pointer will eventually catch up to the slow pointer.

Step-by-step Explanation
Initialization:

Initialize two pointers, slow_pointer and fast_pointer, both pointing to the head node initially.
Cycle Detection:

Traverse the list until the fast_pointer or its next becomes None.
Update slow_pointer and fast_pointer as follows:
slow_pointer = slow_pointer.next
fast_pointer = fast_pointer.next.next
If slow_pointer and fast_pointer meet at some point, return True.
Complexity Analysis
Time Complexity: O(n) — In the worst-case scenario, each node is visited once.
Space Complexity: O(1) — Constant space is used.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head # just the whole list
        fast_pointer = head # also the whole list
        while fast_pointer and fast_pointer.next: # just focus on the fast pointer and the fast_pointer.next up here
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next  # if there is a cycle, fast pointer will eventually equal slow pointer which is a node
            if slow_pointer == fast_pointer:
                return True
        return False

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        current_node = head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next
        return False                                                                 
