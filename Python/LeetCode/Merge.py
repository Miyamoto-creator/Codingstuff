class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


def mergeTwoLists(list1, list2):
    len_lst = []
    len2_lst = []
    start_node = (list1)
    start2_node = (list2)
    while True:
        try:
                len_lst.append(start_node.val)
                len2_lst.append(start2_node.val)
                start_node = start_node.next
                start2_node = start2_node.next
        except AttributeError:
            break 
        print(list1, list2)
        print(list1, list2)
        array = sorted(len_lst + len2_lst)
        return reverseList(array)

def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev

def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

# test cases
t1 = list_to_LL([1, 2, 4])  #ListNode(val=1, next={ListNode(val=2, next={ListNode(val=3, next={ListNode(val=4, next={ListNode(val=5, next={None})})})})})
t2 = list_to_LL([1, 3, 4])  #ListNode(val=1, next={ListNode(val=2, next={None})})
t3 = list_to_LL([])
t4 = list_to_LL([0])

# answers
print()
print(reverseList(t2))
print(reverseList(t3))
print(reverseList(t4))

print(mergeTwoLists(reverseList(t1), reverseList(t2)))
#print(mergeTwoLists(t3, t4))






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         try:
#             list1.val
#         except AttributeError:
#             return list2
#         try:
#             list2.val
#         except AttributeError:
#             return list1
#         len_lst = []
#         len2_lst = []
#         start_node = list1
#         start2_node = list2
#         counter = 0
#         counter1 = 0
#         while True:
#             try:
#                 counter += 1
#                 counter1 += 1
#                 len_lst.append([counter, start_node.val])
#                 len2_lst.append([counter1, start2_node.val])
#                 start_node = start_node.next
#                 start2_node = start2_node.next
#             except AttributeError:
#                 break
#         dl = {}
#         # for i, x in len_lst
#         print(len_lst, "\n", len2_lst)
#         # first header
#         # final header
#         lst = []
#         lst_val = []
#         temp = list1
#         temp2 = list2
#         while True:
#             try:
#                 if temp.val < temp2.val:
#                     lst.append(temp)
#                     lst_val.append(temp.val)
#                     temp = temp.next
#                 elif temp2.val < temp.val:
#                     lst.append(temp2)
#                     lst_val.append(temp2.val)
#                     temp2 = temp2.next
#                 elif temp.val == temp2.val:
#                     lst.append(temp)
#                     lst_val.append(temp.val)
#                     temp = temp.next
#                     lst.append(temp2)
#                     lst_val.append(temp2.val)
#                     temp2 = temp2.next
#             except AttributeError:
#                 break
#         print(lst_val)
#         for i, x in enumerate(lst):
#             if not i == len(lst)-1:
#                 x.next = lst[i+1]
#             else:
#                 x.next = None
#         return lst[0] if not len(lst) == 0 else None
                                
#         lst = [list1.val]
#         print(lst)
#         temp = list1.next
#         print("1 ",temp)
#         lst.append(temp.val)
#         temp = temp.next
#         print("2 ",temp)
#         lst.append(temp.val)
#         temp = temp.next
#         print("3 ",t
#         # while True:
#         #     if temp == None:
#         #         break
#         #     elif 
#         print(lst)
#         print(len(lst))
#         length = len(lst)
        
#         # if list1.val <= list2.val else list2.next