import sys

# USAGE
# turning direction:
#   -l : left
#   -r : right
# action:
#   -e : encrypt
#   -d : decrypt
# key:
#   -k : a binary square matrix writen as string, where each row is separate
#        by a pipe symbol. see the example
#   -s : square matrix side size (optional)
# message:
#   -m : the text that you want encrypt or decrypt
#
# EXAMPLE
# py .\turning.py -e -l -k "1 0 0 0 | 0 0 0 0 | 0 1 0 1 | 0 0 1 0" -m "PLAINTEXT"  :: encrypt
# py .\turning.py -d -r -k "1 0 0 0 | 0 0 0 0 | 0 1 0 1 | 0 0 1 0" -m "CIPHERTEXT" :: decrypt
def main():
  opt = sys.argv[1] # -e to encrypt or -d to decrypt
  dir = get_direction(sys.argv[2])
  K = build_grille(sys.argv[4])
  if opt == "-e":
    ptxt = adjust_to_key(sys.argv[6], K);
    ctxt = encrypt(ptxt, K, dir)
    print(ctxt)
  else:
    ctxt = sys.argv[6]
    ptxt = decrypt(ctxt, K, dir)
    print(ptxt)

def build_grille(str):
    return [ list(map(int, rr.split())) for rr in str.split('|') ]

def get_direction(str):
  if str == "-l":
    return 0
  else:
    return 1

def adjust_to_key(txt, K):
  n = len(K)
  if len(txt) < n*n:
    txt = txt + 'X'*(n*n-len(txt))
  return txt

def encrypt(ptxt, K, dir):
  n = len(K)
  ctxt = [ ['' for i in range(n) ] for i in range(n) ] 
  i = 0
  for t in range(4):
    locs = where_to_write(K)
    for x, y in locs:
      ctxt[x][y] = ptxt[i]
      i += 1
    turn(K, dir)
  return "".join(["".join(row) for row in ctxt])

def decrypt(ctxt, K, dir):
  n = len(K)
  ptxt = []
  ctxt = build_matrix(ctxt, K)
  for t in range(4):
    locs = where_to_write(K)
    for x, y in locs:
      ptxt.append(ctxt[x][y])
    turn(K, dir)
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

def turn(mat, dir):
  n = len(mat)
  if dir == 1:
    for x in range(0, int(n/2)): 
        for y in range(x, n-x-1): 
            temp = mat[y][x] 
            mat[y][x] = mat[n-1-x][y]
            mat[n-1-x][y] = mat[n-1-y][n-1-x]
            mat[n-1-y][n-1-x] = mat[x][n-1-y]
            mat[x][n-1-y] = temp
  else: 
    for x in range(0, int(n/2)): 
        for y in range(x, n-x-1): 
            temp = mat[x][y]
            mat[x][y] = mat[y][n-1-x]
            mat[y][n-1-x] = mat[n-1-x][n-1-y]
            mat[n-1-x][n-1-y] = mat[n-1-y][x]
            mat[n-1-y][x] = temp


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