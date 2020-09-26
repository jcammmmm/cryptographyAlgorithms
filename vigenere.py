ALPHABET_SIZE = 26
CHAR_ASCII_POS = 65

def main():
  key = 'RELATIONS'
  text = 'TO BE OR NOT TO BE THAT IS THE QUESTION'

  tableau = generate_tableau()
  text = format_text(text)
  key = build_key(format_text(key), len(text))

  cyphertext = encrypt(text, key, tableau)
  print(cyphertext)
  plaintext = decrypt(cyphertext, key, tableau)
  print(plaintext)

def encrypt(plaintext, key, tableau):
  cyphertext = []
  for k in range(len(plaintext)):
    j = ord(key[k]) - CHAR_ASCII_POS
    i = ord(plaintext[k]) - CHAR_ASCII_POS
    cyphertext.append(chr(get_symbol(i, j, tableau) + CHAR_ASCII_POS))
  return ''.join(cyphertext)

# we must find for each cyphertext letter -> 26*n complexity, where 
# n is the the lenght of the ct.
def decrypt(cyphertext, key, tableau):
  plaintext = []
  for k in range(len(cyphertext)):
    j = ord(key[k]) - CHAR_ASCII_POS
    i = ord(cyphertext[k]) - CHAR_ASCII_POS
    while i != tableau[j]:
      j += ALPHABET_SIZE
    plaintext.append(chr(j//ALPHABET_SIZE + CHAR_ASCII_POS))
  return ''.join(plaintext)

# The tableau is filled with numbers not letters in order
# to perform generalizations more easily
def generate_tableau():
  tableau = []
  for i in range(ALPHABET_SIZE):
    for j in range(ALPHABET_SIZE):
      c = (i + j)%(ALPHABET_SIZE)
      tableau.append(c)
  return tableau

def format_text(txt):
  return txt.upper().replace(' ','')

# the generated key will always cover the plaint text...
def build_key(key, lenght):
  mask = []
  times = lenght//len(key) + 1
  for i in range(times):
    mask.append(key)
  return ''.join(mask)

def get_symbol(i, j, tableau): 
  return tableau[i*ALPHABET_SIZE + j]
      
if __name__ == '__main__':
  main()