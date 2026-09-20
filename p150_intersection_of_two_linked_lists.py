### brute force first
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

       a = headA
        while a:
            b = headB
            while b:
                if a is b:
                    return a
                b = b.next
            a = a.next
        return None