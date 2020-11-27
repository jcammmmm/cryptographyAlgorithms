def eea(a,b):
  if b == 0:
      return a, 1, 0
  d1,x1,y1 = eea(b, a % b)
  d = d1
  x = y1
  y = x1 - math.floor(a/b) * y1
  return d, x, y