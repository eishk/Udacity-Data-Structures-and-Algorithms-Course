class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    main_set = set()
    if (llist_1.size() == 0 and llist_2.size() == 0):
        return LinkedList()
    elif (llist_1.size() == 0):
        return llist_2
    elif (llist_2.size() == 0):
        return llist_1
    else:
        current = llist_1.head
        while (current is not None):
            main_set.add(current.value)
            current = current.next
        current = llist_2.head
        while (current is not None):
            main_set.add(current.value)
            current = current.next
        new_list = LinkedList()
        for value in main_set:
            new_list.append(value)
        return new_list
    pass

def intersection(llist_1, llist_2):
    if (llist_1.size() == 0 or llist_2.size() == 0):
        return LinkedList()
    else:
        list1 = list()
        current = llist_1.head
        while (current is not None):
            list1.append(current.value)
            current = current.next
        list2 = list()
        current = llist_2.head
        while (current is not None):
            list2.append(current.value)
            current = current.next
        new_list = list()
        for entry in list1:
            if entry in list2 and entry not in new_list:
                new_list.append(entry)
        final = LinkedList()
        for value in new_list:
            final.append(value)
        return final
    pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("Union")
print (union(linked_list_1,linked_list_2))
# Output should be 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print("Intersection")
print (intersection(linked_list_1,linked_list_2))
# Output should be 4 -> 6 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print("Union")
print (union(linked_list_3,linked_list_4))
# Output should be 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print("Intersection")
print (intersection(linked_list_3,linked_list_4))
# Output should be blank


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)
print("Union")
print (union(linked_list_5,linked_list_6))
# Output should be blank
print("Intersection")
print (intersection(linked_list_5,linked_list_6))
# Output should be blank

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [1,2,3,4,5]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)
print("Union")
print (union(linked_list_7,linked_list_8))
# Output should be 1 -> 2 -> 3 -> 4 -> 5
print("Intersection")
print (intersection(linked_list_7,linked_list_8))
# Output should be blank
