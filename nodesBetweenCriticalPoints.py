# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crit_points = []
        prev = head.val
        if not head.next:
            return [-1,-1]

        curr = head.next
        pos = 2
        while curr.next:
            if curr.val < prev and curr.val < curr.next.val:
                crit_points.append(pos)
            
            if curr.val > prev and curr.val > curr.next.val:
                crit_points.append(pos)
            
            prev = curr.val
            pos += 1
            curr = curr.next
        
        res = [float('inf'),float("-inf")]
        if len(crit_points) < 2:
            return [-1,-1]
        else:
            for i in range(len(crit_points)):
                for j in range(i+1,len(crit_points)):
                    res[0] = min(res[0],abs(crit_points[j]-crit_points[i]))
                    res[1] = max(res[1],abs(crit_points[j]-crit_points[i]))
        
        return res
