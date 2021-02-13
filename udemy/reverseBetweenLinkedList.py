"""
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in one-pass.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

from LinkedList import LinkedList 

def reverseBetween(head, m, n):
	if m == n or n == 1:
		return head

	curnode = start = head
	curpos = 1
	while curpos < m:
		start = curnode
		curnode = curnode.next
		curpos += 1

	newlist = None
	tail = curnode

	while m <= curpos <= n:
		next = curnode.next
		curnode.next = newlist
		newlist = curnode
		curnode = next
		curpos += 1	

	if m == 1:
		head = newlist	
	start.next = newlist 
	tail.next = curnode
			
	ptr = head
	l = []
	while ptr:
		print (ptr.value)
		l.append(ptr.value)
		ptr = ptr.next
	return head
			
def create_linked_list(arr):
	l = LinkedList()
	for i in arr:
		l.append(i)
	l.prin()
	return l.head 

m = 1 
n = 4 
s = [10,22,13,4,5,23,1,24,16,8]
#s = [1,2,3,4,5]
#m = 1
#n = 2
head = create_linked_list(s)
print (reverseBetween(head,m, n)) 

