class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listNodeCreator(listing:list[int]):
    head = None
    for val in reversed(listing):
        head = ListNode(val, head)
    return head

class Solution:
    def addTwoNumbers(self, l1: list, 
                      l2: list) -> list[int]:
        
        glorb:list = []
        while l1:
            glorb.append(l1.val)
            l1 = l1.next
        glorb.reverse()

        glurb:list = []
        while l2:
            glurb.append(l2.val)
            l2 = l2.next
        glurb.reverse()

        list(str(glorb))
        list(str(glurb))

        l1_str:str = ''
        for i in glorb:
            l1_str += str(i)
        l2_str:str = ''
        for i in glurb:
            l2_str += str(i)
        
        l3 = list(str(int(l1_str) + int(l2_str)))
        l3.reverse()
        return listNodeCreator(l3)
    

    
solution:Solution = Solution()
print(solution.addTwoNumbers([2,4,3], [5,6,4]))