def addto80(n):
       return n + 80

cache = {}

def memoizedaddto80(n):
       val = cache.get(n, None)
       if val:
               print ('from cache')
               return val
       cache[n] = n + 80
       return cache[n]

#print (memoizedaddto80(5))
#print (memoizedaddto80(5))
#print (memoizedaddto80(5))

def memoizedadd80():
  cache = {}

  def memoized(n):
          val = cache.get(n, None)
          if val:
             print ('from cache')
             return val
          cache[n] = n + 80
          return cache[n]

  return memoized


memo = memoizedadd80()
print (memo(3))
print (memo(3))
print (memo(3))
print (memo(3))


