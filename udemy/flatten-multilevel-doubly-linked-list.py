"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Input: head = [1,2,null,3]
Output: [1,3,2]

Input: head = []
Output: []

"""

def flatten(head):
	child_nodes = []
        ptr = head
        while ptr:
            ch = ptr.child
            nx = ptr.next
            if ch and nx:
                child_nodes.append(nx)
            if ch:
                ptr.child = None
                ptr.next = ch
                parent = ptr
                ptr = ch
                ptr.prev = parent
            else:
                prev = ptr
                ptr = ptr.next
            
            if ptr is None and child_nodes:
                popped = child_nodes.pop()
                prev.next = popped
                ptr = popped
                ptr.prev = prev
                
        return head
