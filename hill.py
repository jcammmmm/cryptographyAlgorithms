import numpy as np

BLOCK_SIZE = 2

def main():
  key = "93 39 3 23429 29 20 2 32 10"
  key = build_matrix(key)
  print(key)
  pass

def encrypt(key, plaintext):
  blocks = [(plaintext[i:i + BLOCK_SIZE]) for i in range(0, len(plaintext), BLOCK_SIZE)] 

def encrypt_block(block, matrix):
  pass

def check_matrix_key(matrix_key):
  A = matrix_key
  detA = np.det
  pass

def build_matrix(str_key):
  num_key = [int(i) for i in str_key.split(' ')];
  m_size = np.sqrt(len(num_key))
  if not m_size.is_integer():
    raise Exception("LA MATRIZ NO ES CUADRADA")
  return np.reshape(num_key, (int(m_size), int(m_size)))


if __name__ == '__main__':
  main()