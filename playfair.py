# Our alphabet does not contain 'I' vowel letter, see formatText procedure.
# Also, every processed text is uppercases.
BLOCK_SIZE = 2
MATRIX_SIZE = 5

def main():

  # TODO remove repeated chars from key
  key = "yoanpiz" # input("clave: \n")
  option = 1

  pt = "this secret message is encrypted" # input("texto claro: \n")
  print(formatText(pt))

  ct = encrypt(key, pt)
  print(ct)
  dt = decrypt(key, ct)
  print(dt)


def encrypt(key, plaintext):
  key_matrix = build_key_matrix(key)
  # plaintext format
  plaintext = formatText(plaintext)
  ciphertext = "";
  blocks = [(plaintext[i:i + BLOCK_SIZE]) for i in range(0, len(plaintext), BLOCK_SIZE)] 
  for block in blocks:
    X, Y = encrypt_block(block, key_matrix)
    ciphertext += X + Y
  return ciphertext

  
def encrypt_block(block, key_matrix):
  encrypted_block = ['','']

  r1, c1 = get_coordinates(block[0], key_matrix)
  r2, c2 = get_coordinates(block[1], key_matrix)

  if r1 != r2 and c1 != c2:
    encrypted_block[0] = get_letter(r1, c2, key_matrix)
    encrypted_block[1] = get_letter(r2, c1, key_matrix)
  elif r1 == r2:
    encrypted_block[0] = get_letter(r1, (c1 + 1)%MATRIX_SIZE, key_matrix)
    encrypted_block[1] = get_letter(r2, (c2 + 1)%MATRIX_SIZE, key_matrix)
  elif c1 == c2: 
    encrypted_block[0] = get_letter((r1 + 1)%MATRIX_SIZE, c2, key_matrix)
    encrypted_block[1] = get_letter((r2 + 1)%MATRIX_SIZE, c2, key_matrix)
  # The case when both r1, r2 and c1, c2 are equals doesnt happen since we
  # do not have concecutive letters...
  else:
    raise Exception("Logic error same letter are in the same")
  return encrypted_block[0], encrypted_block[1]

# same as encrypt but var names are changed...
def decrypt(key, ciphertext):
  key_matrix = build_key_matrix(key)
  # formatting
  plaintext = "";
  blocks = [(ciphertext[i:i + BLOCK_SIZE]) for i in range(0, len(ciphertext), BLOCK_SIZE)] 
  for block in blocks:
    X, Y = decrypt_block(block, key_matrix)
    plaintext += X + Y
  return plaintext

# same as encrypt_block but reversed...
def decrypt_block(block, key_matrix):
  decrypted_block = ['','']

  r1, c1 = get_coordinates(block[0], key_matrix)
  r2, c2 = get_coordinates(block[1], key_matrix)

  if r1 != r2 and c1 != c2:
    decrypted_block[0] = get_letter(r1, c2, key_matrix)
    decrypted_block[1] = get_letter(r2, c1, key_matrix)
  elif r1 == r2:
    decrypted_block[0] = get_letter(r1, (c1 - 1)%MATRIX_SIZE, key_matrix)
    decrypted_block[1] = get_letter(r2, (c2 - 1)%MATRIX_SIZE, key_matrix)
  elif c1 == c2: 
    decrypted_block[0] = get_letter((r1 - 1)%MATRIX_SIZE, c2, key_matrix)
    decrypted_block[1] = get_letter((r2 - 1)%MATRIX_SIZE, c2, key_matrix)
  # The case when both r1, r2 and c1, c2 are equals doesnt happen since we
  # do not have concecutive letters...
  else:
    raise Exception("Logic error same letter are in the same")
  return decrypted_block[0], decrypted_block[1]


def get_coordinates(letter, key_matrix):
  index = key_matrix.index(letter)
  i = index//MATRIX_SIZE
  j = index%MATRIX_SIZE
  return i, j

def get_letter(i, j, key_matrix): 
  return key_matrix[i*MATRIX_SIZE + j]

def formatText(text):
  text = text.upper().replace("I", "J").replace(' ','')

  cprev = ' '
  for i in range(len(text)):
    ccurr = text[i]
    if ccurr == cprev and i%2 == 1:
      text = text[:i - 1] + "X" + text[i - 1:]
    cprev = ccurr

  if len(text)%2 == 1: 
    text += "X"
  return text

def formatKey(key):
  return key.upper().replace("I", "J").replace(' ','')

def build_key_matrix(key):
  # key format
  key = formatKey(key)

  # alphabet format
  chars = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
  key_set = {c : 0 for c in key}

  # compute chars - key
  chars_minus_k = {}
  for c in chars:
    if c not in key_set:
      chars_minus_k[c] = 0;

  # build the key map
  kmatrix = [0 for i in range(MATRIX_SIZE*MATRIX_SIZE)]
  j = 0
  for k in key:
    kmatrix[j] = k
    j += 1
  for i in chars_minus_k:
    kmatrix[j] = i
    j += 1
  return kmatrix

if __name__ == "__main__":
  main()