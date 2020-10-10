# class Node:
#     def __init__(self, item, next):
#         self.item = item
#         self.next = next
#
# class Stack:
#     def __init__(self):
#         self.last = None
#
#     def push(self,item):
#         self.last = Node(item, self.last)
#
#     def pop(self):
#         item = self.last.item
#         self.last =self.last.next
#         return item
#
# s = Stack()
# s.push(())
# s.push([])
# s.push({})

s=')'

stack =[]
table = {
    ')':'(',
    '}':'{',
    ']':'['
}
print(table[']'])


# for char in s:
#     if char not in table:
#         stack.append(char)
#     elif not stack or table[char] != stack.pop():
#         print (False)
# print(len(stack) ==0)

