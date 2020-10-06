def main():
  txt = 'JIMATTACKSATDAWN'
  grille = "1 0 0 0 | 0 0 0 0 | 0 1 0 1 | 0 0 1 0"
  K = [ list(map(int, rr.split())) for rr in grille.split('|') ]
  encrypt(txt, K)

def encrypt(ptxt, K):
  n = len(K)
  ctxt = [ ['' for i in range(n) ] for i in range(n) ] 
  i = 0
  for t in range(4):
    locs = where_to_write(K)
    for x, y in locs:
      ctxt[x][y] = ptxt[i]
      i += 1
    turn(K)
    print_grille(ctxt)

def where_to_write(K):
  locs = []
  n = len(K)
  for i in range(n):
    for j in range(n):
      if K[i][j] == 1:
        locs.append((i, j))
  return locs

# 90 deg. right rotation
def turn(mat):
    n = len(mat)
    for x in range(0, int(n/2)): 
        for y in range(x, n-x-1): 
            temp = mat[y][x] 
            mat[y][x] = mat[n-1-x][y]
            mat[n-1-x][y] = mat[n-1-y][n-1-x]
            mat[n-1-y][n-1-x] = mat[x][n-1-y]
            mat[x][n-1-y] = temp
  
def print_grille(mat):
    n = len(mat)
    for i in range(0, n): 
        for j in range(0, n): 
            print (str(mat[i][j]).rjust(3), end = ' ')
        print ("") 
  
def validate_operation(txt, mat):
  n = len(mat)
  if (len(txt) > n*n):
    raise Exception("The plaintext is bigger than turning grille.")

if __name__ == "__main__":
  main()