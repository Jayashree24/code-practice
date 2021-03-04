"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
fib(6) = 8
"""
cal = 0
dp_cal = 0

def fibonacci_recursive(n):
        global cal
        cal += 1
        x = y = 0
        if n < 2:
            return n
        else:
            return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

def fib_dp():
       cache = {}
       def fib(n):
               global dp_cal
               dp_cal += 1
               #print ("fib for %d" % n)
               val = cache.get(n, None)
               if val:
                       #print ("Getting %d=%d from cache" % (n, cache[n]))
                       return val
               if n < 2:
                       cache[n] = n
               else:
                       cache[n] = fib(n-2) + fib(n-1)
               return cache[n]
       return fib

def fib_iter(n):
       arr = [0, 1]
       for i in range(2, n+1):
               arr.append(arr[i-1] + arr[i-2])
       return arr[-1]

f = fib_dp()
print ('DP : %s' % f(10))
print ('DP operations : %s' % dp_cal)
#print ('*****')
#print (f(6))
#print ('*****')
#print (f(7))

print ('Recursive : %s' % fibonacci_recursive(10))
print ('Recursive operations : %s' % cal)

print (fib_iter(10))


