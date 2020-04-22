from math import *
from decimal import *
import warnings
from time import perf_counter

getcontext().prec = 128


#A small percentage of products have an m thats massive, in the tens or hundreds of thousands
#for 64 bit numbers, so aren't practical to factor faster than simply checking every
#prime from 2 to < sqrt(p)

print("note: doesn't trim leading or trailing spaces. Default is 0, or 'no cutoff time'")
print("note: products should be entered WITHOUT grouping symbols such as commas")
print("\n")

cutoffStr = input("Max minutes to run: ")
try:
  cutofftime = int(cutoffStr)
except ValueError:
  print("No max time cutoff specified. Defaulting to unlimited.")
  cutofftime = 0


pStr = input("enter product: ")
try:
  p = Decimal(pStr)
except Exception:
  print("Not a number. Defaulting to 48 bit test product 174135918609547")
  p = Decimal('174135918609547')




cutofftime = cutofftime * 60



phi = Decimal((sqrt(5)+1)/2)


def hana(p, startTime, cutoff=60*480):
  print("cutoff minutes: " + str(cutoff))
  w = p.sqrt()
  h = Decimal(log(p, phi))
  
  i = floor(w/h)
  j = 1/((i*h)/w)
  
  k = floor((h*phi).sqrt())
  n = 0 #initial search value
  f = i+1 #just initializing with a placeholder value for now
  m = 0
  t = 0
  
  while n <= i:
    f = 1 + ceil(floor(w/h))-n
    m = 0
    
    
    #while m <= k:
    while m <= 68:
      if t < 1:
        print("f: " + str(f) + ",  m: " + str(m) + ", floor(f*h)+m: " + str(floor(f*h)+m))
        t = 1000
      
      t = t - 1
      if (p/(floor(f*h)+m)) % 1 == 0 and (p/(floor(f*h)+m)) < p:
        print("FACTOR FOUND: " + str(floor(f*h)+m))
        print("f: " + str(f) + ",  m: " + str(m) + ", floor(f*h)+m: " + str(floor(f*h)+m))
        print("PRODUCT: " + str(p))
        return p/(floor(f*h)+m)
      else:
        m = m + 1
        
    n = n + 1
    if n >= i:
      return n
      
    if (perf_counter() - startTime) > cutoff and cutoff != 0:
      print("CUTOFF REACHED. EXITING.")
      return False

      
def getM(p, a):
    w = p.sqrt()
    h = Decimal(log(p, phi))
    result = ceil(a - floor(a/h)*h)
    print("m: " + str(result))
    a - (floor(a/h)*h)
    return result



#getM(p, a)
startTime = perf_counter()
hana(p, startTime, cutofftime)

print("duration: ")
print(str(perf_counter() - startTime) + "s\n")