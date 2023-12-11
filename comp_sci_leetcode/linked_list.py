# Create a Node class to create a node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# # Create a LinkedList class
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     # Method to add a node at begin of LL
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head # the next has to be taken care of first, otherwise you lost track of the current head.
#             self.head = new_node
#
#     # Method to add a node at any index
#     # Indexing starts from 0.
#     def insert_at_index(self, data, index):
#         new_node = Node(data)
#         current_node = self.head
#         position = 0
#         if position == index:
#             self.insert_at_beginning(data)
#         else:
#             while current_node is not None and position + 1 != index:
#                 position = position + 1
#                 current_node = current_node.next
#
#             if current_node is not None:  # when position + 1 == index
#                 new_node.next = current_node.next   # the node one behind where the new node should be inserted is current_node
#                 current_node.next = new_node       # we want to do this: from CN -> CN.next  to CN -> new_node -> CN.next
#             else:
#                 print("Index not present")
#
#     # Method to add a node at the end of LL
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#
#         current_node.next = new_node # this makes sense. traverse to the end (current node has no next, and then set
#         # current_node.next as the new_node)
#
#     # Update node of a linked list
#     # at given position
#     def updateNode(self, val, index):
#         current_node = self.head
#         position = 0
#         if position == index:
#             current_node.data = val
#         else:
#             while current_node is not None and position != index:
#                 position = position + 1
#                 current_node = current_node.next
#
#             if current_node is not None:
#                 current_node.data = val
#             else:
#                 print("Index not present")
#
#     # Method to remove first node of linked list
#
#     def remove_first_node(self):
#         if self.head is None:
#             return
#
#         self.head = self.head.next
#
#     # Method to remove last node of linked list
#     def remove_last_node(self):
#
#         if self.head is None:
#             return
#
#         current_node = self.head
#         while current_node.next.next:  # so current_node is the third to last_node
#             current_node = current_node.next
#
#         current_node.next = None   # ah so we need to get to the second to last node so we can set the CN.next to None
#
#     # Method to remove at given index
#     def remove_at_index(self, index):  # to forget a node, we need to point the previous node at index - 1 to either None or the node_at_index.next
#         if self.head is None:
#             return
#
#         current_node = self.head
#         position = 0
#         if position == index:
#             self.remove_first_node()
#         else:
#             while current_node is not None and position + 1 != index:
#                 position = position + 1
#                 current_node = current_node.next
#
#             if current_node is not None:
#                 current_node.next = current_node.next.next  # this is what we need to forget a node in the middle. we cannot do anything to the node we're trying to forget. the node before matters and the node after matters.
#             else:
#                 print("Index not present")
#
#     # Method to remove a node from linked list
#     def remove_node(self, data):
#         current_node = self.head
#
#         if current_node.data == data:
#             self.remove_first_node()
#             return
#
#         while current_node is not None and current_node.next.data != data:
#             current_node = current_node.next
#
#         if current_node == None:
#             return
#         else:
#             current_node.next = current_node.next.next
#
#     # Print the size of linked list
#     def size_of_list(self):
#         size = 0
#         if (self.head):
#             current_node = self.head
#             while (current_node):
#                 size = size + 1
#                 current_node = current_node.next
#             return size
#         else:
#             return 0
#
#     # print method for the linked list
#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next
#
#     def return_list(self):
#         list_holder = []
#         current_node = self.head
#         while current_node:
#             list_holder.append(current_node.data)
#             current_node = current_node.next
#
#         return list_holder

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        current_node = self.head

        if self.head is None:
            self.head = new_node
            return

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index):
        position = 0
        current_node = self.head
        new_node = Node(data)
        while current_node.next is not None and position + 1 != index:
            current_node = current_node.next
            position += 1

        new_node.next = current_node.next  # we want to go from position_node -> position_node.next to position_node -> new_node -> position_node.next
        current_node.next = new_node

    def remove_first_node(self):
        self.head = self.head.next

    def remove_last_node(self):
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        position = 0
        current_node = self.head

        while current_node.next and position + 1 != index:
            current_node = current_node.next
            position += 1

        current_node.next = current_node.next.next

    def update_node(self, data, index):
        current_node = self.head
        position = 0
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head.next
            self.head = new_node
            return

        while current_node.next and position + 1 != index:
            current_node = current_node.next
            position += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def size_of_list(self):
        size = 0
        current_node = self.head

        while current_node is not None:
            size += 1
            current_node = current_node.next

        return size

    def print_list(self):
        print_list = []
        current_node = self.head
        while current_node:
            print_list.append(current_node.data)
            current_node = current_node.next

        return "-->".join(print_list)


    def return_list(self):
        linked_list_data = []
        current_node = self.head
        while current_node:
            linked_list_data.append(current_node.data)
            current_node = current_node.next

        return linked_list_data

# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insert_at_end('a')
assert llist.return_list() == ['a']
llist.insert_at_end('b')
assert llist.return_list() == ['a', 'b']
llist.insert_at_beginning('c')
assert llist.return_list() == ['c', 'a', 'b']
llist.insert_at_end('d')
assert llist.return_list() == ['c', 'a', 'b', 'd']
llist.insert_at_index('g', 2)
assert llist.return_list() == ['c', 'a', 'g', 'b', 'd'], f"this is not equal {llist.return_list()}"

# print the linked list
print("Here's how the link list appears. the list should be c -> a -> g -> b -> d: ", llist.print_list())

assert llist.return_list() == ['c', 'a', 'g', 'b', 'd'], f"list does not equal {llist.return_list()}"

# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
assert llist.return_list() == ['a', 'g', 'b', 'd']
print("Remove Last Node")
llist.remove_last_node()
assert llist.return_list() == ['a', 'g', 'b']
print("Remove Node at Index 1")
llist.remove_at_index(1)
assert llist.return_list() == ['a', 'b']

# print the linked list again
print("\nLinked list after removing some nodes:")
llist.print_list()

print("\nUpdate node Value")
llist.update_node('z', 0)
assert llist.return_list() == ['z', 'b'], f"this is the new list: {llist.return_list()}"
llist.print_list()

print("\nSize of linked list :", end=" ")
assert llist.size_of_list() == 2
print(llist.size_of_list())


# can these methods handle odd sized list like a list of size 2
llist2 = LinkedList()

# add nodes to the linked list
llist2.insert_at_end('a')
llist2.insert_at_end('b')

print('does this owrk?')
llist2.remove_at_index(1)
llist2.print_list()
