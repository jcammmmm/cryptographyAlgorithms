import math

def eea(a,b):
  if b == 0:
      return a, 1, 0
  d1,x1,y1 = eea(b, a % b)
  d = d1
  x = y1
  y = x1 - math.floor(a/b) * y1
  return d, x, y



# for i in range(2,9):
#     d, x, y = eea(i, 9)
#     if d == 1:
#       # print (x, 9)
#       print ('1 - %1d * %3d = %3d'%(i, x, 1- i*x))

