"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Input: head = [1,2,null,3]
Output: [1,3,2]
"""
def flatten(head):
	curnode = head
        while curnode:
                childnode = curnode.child
                if childnode:
                    curnode.child = None
                    prev = curnode.next
                    curnode.next = childnode
                    childnode.prev = curnode
                    while childnode.next:
                        childnode = childnode.next
                    childnode.next = prev
                    if prev:
                        prev.prev = childnode
                curnode = curnode.next
	return head


