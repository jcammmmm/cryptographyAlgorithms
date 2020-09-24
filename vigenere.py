ALPHABET_SIZE = 26
CHAR_ASCII_POS = 65

def main():
  key = 'RELATIONS'
  text = 'TO BE OR NOT TO BE THAT IS THE QUESTION'

  tableau = generate_tableau()
  text = format_text(text)
  key = build_key(format_text(key), len(text))

  print(encrypt(text, key, tableau))

def encrypt(plaintext, key, tableau):
  cyphertext = []
  for k in range(len(plaintext)):
    j = ord(plaintext[k]) - CHAR_ASCII_POS
    i = ord(key[k]) - CHAR_ASCII_POS
    cyphertext.append(chr(get_symbol(i, j, tableau) + CHAR_ASCII_POS))
  return cyphertext

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
  TABLEAU = generate_tableau()
  main()