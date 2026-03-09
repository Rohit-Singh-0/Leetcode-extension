# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        temp = l1
        while temp:
            num1.append(str(temp.val))
            temp = temp.next
        num2 = []
        temp = l2
        while temp:
            num2.append(str(temp.val))
            temp = temp.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        num1 = int("".join(num1))
        num2 = int("".join(num2))
        num_sum = num1+num2
        ans = []
        for i in str(num_sum):
            ans.append(int(i))
        ans = ans[::-1]
        temp = ListNode(ans[0])
        head= temp
        for i in ans[1:]:
            node = ListNode(i)
            temp.next = node
            temp = temp.next
        return head