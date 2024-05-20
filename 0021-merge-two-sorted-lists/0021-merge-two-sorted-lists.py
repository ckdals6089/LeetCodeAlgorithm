# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the head of the new list
        dummy = ListNode()
        # Use a pointer to construct the new list
        current = dummy

        # While both lists have nodes left to process
        while list1 and list2:
            if list1.val <= list2.val:
                # If the value of the node in list1 is less than or equal to the value of the node in list2
                # Add the node from list1 to the new list
                current.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # If the value of the node in list2 is less than the value of the node in list1
                # Add the node from list2 to the new list
                current.next = list2
                # Move to the next node in list2
                list2 = list2.next
            # Move the pointer of the new list
            current = current.next

        # If there are remaining nodes in either list1 or list2, add them to the new list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # The head of the merged list is the next node of the dummy node
        return dummy.next        