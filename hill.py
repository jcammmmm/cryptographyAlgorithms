import numpy as np
import sys

BLOCK_SIZE = 2
ALPHABET_SIZE = 26

# Example usage:
# py .\hill.py -e -k "11 8 3 7" -m "PLAINTEXT"  :: encrypt
# py .\hill.py -d -k "11 8 3 7" -m "CIPHERTEXT" :: decrypt
# py .\hill.py -g                               :: generate
def main():
  # cyphertext = "VKFZRVWTIAZSMISGKA"
  opt = sys.argv[1] # should be -e to encrypt or -d to decrypt
  if opt == "-e":
    key = sys.argv[3]
    plaintext = sys.argv[5]
    cyphertext = encrypt(key, plaintext)
    print(cyphertext)
  elif opt == "-d":
    key = sys.argv[3]
    cyphertext = sys.argv[5]
    plaintext = decrypt(key, cyphertext)
    print(plaintext)
  else:
    K = get_valid_matrix(2)
    print(np.reshape(K, -1))

def encrypt(key, plaintext):
  key = build_matrix(key)
  check_matrix(key)
  return multiply_and_concat(key, plaintext)

def decrypt(key, cyphertext):
  key = build_matrix(key)
  check_matrix(key)
  key_inv = get_modular_inverse_matrix(key)
  return multiply_and_concat(key_inv, cyphertext)
  
def multiply_and_concat(matrix, text):

  text = to_nums(text)
  blocks = [(text[i:i + BLOCK_SIZE]) for i in range(0, len(text), BLOCK_SIZE)]
  out = []
  for b in blocks:
    c = np.matmul(b, matrix)
    out.append(c[0]%ALPHABET_SIZE)
    out.append(c[1]%ALPHABET_SIZE)
  return to_text(out)

def check_matrix(matrix):
  A = matrix
  
  detA = int(np.round(np.linalg.det(A)))
  # has modular inverse? 
  # gcd(x, y) = (d, a, b) :: ax + by = d
  # if d = 1 => ax + by = 1 -> ax - 1 = -by
  (d, a, b) = egcd(detA, ALPHABET_SIZE)
  if d != 1:
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
  return M

def get_modular_inverse_matrix(matrix):
  det = int(np.round(np.linalg.det(matrix)))
  d, a, b = egcd(det, ALPHABET_SIZE)
  
  # as d = 1 => ax + by = 1 -> ax - 1 = -by
  if d == 1:
    M = matrix
    M_adj = [[0, 0], [0, 0]]
    M_adj[0][0] =  M[1][1]
    M_adj[0][1] = -M[0][1]
    M_adj[1][0] = -M[1][0]
    M_adj[1][1] =  M[0][0]
    M = np.array(M_adj)*a
    return M
  else:
    raise Exception("LA MATRIZ NO TIENE INVERSA MODULO " + str(ALPHABET_SIZE))
    


def build_matrix(str_key):
  num_key = [int(i) for i in str_key.split(' ')];
  m_size = np.sqrt(len(num_key))
  if m_size != 2:
    raise Exception("LA MATRIZ NO ES 2X2")

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