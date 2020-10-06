import sys

# py .\turning.py -e -k "1 0 0 0 | 0 0 0 0 | 0 1 0 1 | 0 0 1 0" -m "PLAINTEXT"  :: encrypt
# py .\turning.py -d -k "1 0 0 0 | 0 0 0 0 | 0 1 0 1 | 0 0 1 0" -m "CIPHERTEXT" :: decrypt
def main():
  opt = sys.argv[1] # -e to encrypt or -d to decrypt
  K = build_grille(sys.argv[3])
  if opt == "-e":
    ptxt = adjust_to_key(sys.argv[5], K);
    ctxt = encrypt(ptxt, K)
    print(ctxt)
  else:
    ctxt = sys.argv[5]
    ptxt = decrypt(ctxt, K)
    print(ptxt)

def build_grille(str):
    return [ list(map(int, rr.split())) for rr in str.split('|') ]

def adjust_to_key(txt, K):
  n = len(K)
  if len(txt) < n*n:
    txt = txt + 'X'*(n*n-len(txt))
  return txt

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
  return "".join(["".join(row) for row in ctxt])

def decrypt(ctxt, K):
  n = len(K)
  ptxt = []
  ctxt = build_matrix(ctxt, K)
  for t in range(4):
    locs = where_to_write(K)
    for x, y in locs:
      ptxt.append(ctxt[x][y])
    turn(K)
  return "".join(ptxt)

def build_matrix(ctxt, K):
  n = len(K)
  return [list(ctxt[i:i+n]) for i in range(0, len(ctxt), n)] 


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