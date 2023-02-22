# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def printNodes(node):
            ptr = node
            print(ptr.val)
            while ptr.next:
                ptr = ptr.next
                print(ptr.val)

        printNodes(head)
        if head.next.next != None:            
            length = 1
            ptr1 = head
            while ptr1.next != None:
                length += 1
                ptr1 = ptr1.next

            toMove = length//2 if length%2==0 else (length//2)+1
            print('Move:', toMove, length)
            ptr1 = head
            slow = ptr1
            for i in range(toMove):
                ptr1 = ptr1.next
                if i != 0: slow = slow.next
            slow.next = None
            print('Second list')
            printNodes(ptr1)

            ptr2 = ptr1 # both pointing to second part of list
            if length in [4, 5]:
                temp = ptr2
                ptr2 = ptr2.next
                ptr2.next = temp
                temp.next = None
            elif length > 5:
                ptr2 = ptr1.next
                ptr1.next = None
                while ptr2.next:
                    prev = ptr1
                    ptr1 = ptr2
                    ptr2 = ptr2.next
                    ptr1.next = prev
                ptr2.next = ptr1
        
            print('After reversal')
            printNodes(head)
            print('Part 2')
            printNodes(ptr2)
    
            # merge two lists
            ptr1 = head
            while ptr1.next:
                temp2 = ptr2.next
                ptr2.next = ptr1.next
                ptr1.next = ptr2
                ptr1 = ptr2.next
                ptr2 = temp2
    
            if ptr2:
                ptr1.next = ptr2

