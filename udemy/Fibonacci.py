"""
Fibonacci sequence
Given a number N return the index value of the Fibonacci
sequence, where the sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21

For example: fibonacciRecursive(6) should return 8

"""

def fibonacci_recursive(n):
        #print ("n=%s" % n)
        x = y = 0
        if n == 0:
                return 0
        elif n == 1:
                return 1
        else:
                #x = fibonacci_recursive(n-1)
                #y = fibonacci_recursive(n-2)
                #print ("[%s] x=%s y = %s" % (n, x, y))
                return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))
   

def fibonacci_iterative(n):
        first_prev = 0
        second_prev = 1
        if n == 0:
                return 0
        elif n == 1:
                return 1
        for i in range(2, n+1):
                #print (first_prev, second_prev)
                temp = second_prev
                second_prev = second_prev + first_prev
                first_prev = temp
        return (second_prev)

		 
print (fibonacci_iterative(10))
print (fibonacci_recursive(10))
