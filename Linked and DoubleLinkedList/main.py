# # ===================================================Связанный список

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def display(self):
#         result = []
#         current = self.head
#         while current:
#             result.append(current.data)
#             current = current.next
#         print(result)

#     def remove(self, data):
#         if not self.head:
#             return

#         if self.head.data == data:
#             self.head = self.head.next
#             return

#         current = self.head
#         while current.next:
#             if current.next.data == data:
#                 current.next = current.next.next
#                 return
#             current = current.next

# li = LinkedList()
# li.add(10)
# li.add(20)
# li.add(30)
# li.add(40)
# li.display()
# li.remove(40)
# li.display()



# =====================================================Двусвязный список
# class DNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# node1 = DNode(10)
# node2 = DNode(20)
# node3 = DNode(30)


# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2



# current = node1
# while current:
#     print(current.data)
#     current = current.next


# current = node3
# while current:
#     print(current.data)
#     current = current.prev












# ===================================================================================================================
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def __len__(self):
#         return self.size 

#     def is_empty(self):
#         return self.head is None


#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#         self.size += 1

#     def find(self, data):
#         current = self.head
#         index = 0
#         while current:
#             if current.data == data:
#                 return index
#         current = current.next
#         index += 1
#         return -1

#     def clear(self):
#         self.head = Node
#         self.head = 0

#     def delete_at_index(self, index):
#         if index < 0 or index >= self.size:
#             raise IndexError('index out linkedlist range')
        

#         current = self.head
#         if index == 0:
#             self.head = current.next
#         else:
#             prev = None
#             for _ in range(index):
#                 prev = current
#                 current = current.next
#             prev.next = current.next
#         self.size -= 1
#         return current.data

#     def contains(self, data):
#         return self.find(data) != -1


#     def __str__(self):
#         return "->".join(str(x) for x in self.to_list())

#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev





    

