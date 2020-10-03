import numpy as np

BLOCK_SIZE = 2
ALPHABET_SIZE = 26

def main():
  key = "11 8 3 7"
  plaintext = "JULY"
  key = build_matrix(key)
  check_matrix(key)
  opt = "-e"
  if opt == "-e":
    print(encrypt(key, plaintext))

  else: 
    pass
  # get_valid_matrix(2)

def encrypt(key, plaintext):
  plaintext = to_nums(plaintext)
  
  blocks = [(plaintext[i:i + BLOCK_SIZE]) for i in range(0, len(plaintext), BLOCK_SIZE)]
  cyphertext = []
  for b in blocks:
    c = np.matmul(b, key)
    cyphertext.append(c[0]%ALPHABET_SIZE)
    cyphertext.append(c[1]%ALPHABET_SIZE)

  cyphertext = to_text(cyphertext)
  return "".join(cyphertext)

def encrypt_block(block, matrix):
  pass

def check_matrix(matrix):
  A = matrix
  detA = int(np.round(np.linalg.det(A)))
  # has modular inverse? 
  # gcd(x, y) = (d, a, b) :: ax + by = d
  # if d = 1 => ax + by = 1 -> ax - 1 = -by
  (d, a, b) = egcd(detA, ALPHABET_SIZE)
  if d != 1:
    print("LA MATRIZ NO TIENE INVERSA MODULAR, SU DETERMINANTE NO ES 1.")
    return False
  else:
    return True
  
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def get_valid_matrix(size):
  mat_ok = False
  M = []
  while not mat_ok:
    M = [np.random.randint(15) for i in range(size*size)]
    M = np.reshape(M, (size, size))
    mat_ok = check_matrix(M)
  print(M)
    

def build_matrix(str_key):
  num_key = [int(i) for i in str_key.split(' ')];
  m_size = np.sqrt(len(num_key))
  if not m_size.is_integer():
    raise Exception("LA MATRIZ NO ES CUADRADA")
  return np.reshape(num_key, (int(m_size), int(m_size)))

def to_nums(text):
  text = text.upper().replace(' ','')
  nums = [ord(c) - 65 for c in text]
  if len(nums)%2 != 0: nums.append(ord('X'))
  return nums

def to_text(nums):
  text = [chr(i + 65) for i in nums]
  return "".join(text)


if __name__ == '__main__':
  main()