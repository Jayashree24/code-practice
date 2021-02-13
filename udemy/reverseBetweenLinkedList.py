"""
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in one-pass.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

from LinkedList import LinkedList 

def reverseBetween(head, m, n):
	start = None
	first = head
	second = first.next
	i = 0
	while second:
		print (i, first.value, second.value)
		if n == 1 or m == n:
			return head
		if m-2 <= i <= n-2:
			if not start:
				start = first
				print ("start=%s %s" % (start.value, start.next.value))	
			temp = second.next
			second.next = first
			first = second
			second = temp
			print (i, first.value, second.value)
			end = first 
			end_next = second 
			print ('end=%s %s %s' % (end.value, end_next.value, temp.value))
		else:
			first = second 
			second = first.next
		i += 1

	if start:
		print ("start=%s %s %s %s" % (start.value, start.next.value, end.value, end.next.value))
		if m == 1:
			print ('heee')
			start.next = end_next
			head = end
		else:
			temp = start.next
			start.next = end
			temp.next = end_next
		print ("start=%s %s %s %s" % (start.value, start.next.value, end.value, end.next.value))

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

m = 2 
n = 4 
s = [10,22,13,4,5,23,1,24,16,8]
#s = [1,2,3,4,5]
#m = 1
#n = 2
head = create_linked_list(s)
print (reverseBetween(head,m, n)) 

