import pyDes
import pyaes
import base64
import sys
import hashlib
import os

# Usage
# py aes.py 128 
def main():
  mode = sys.argv[1]
  in_path = sys.argv[2]
  out_path = sys.argv[3]

  # Open plain image
  with open(in_path, "rb") as file:
    img_in = bytearray(file.read())

  # enc
  key = get_random_key(mode)
  AES = pyaes.AESModeOfOperationCTR(key)
  ptxt_b64 = base64.b64encode(img_in)
  ctxt = AES.encrypt(ptxt_b64)
  ctxt_b64 = base64.b64encode(ctxt)

  # dec
  AES = pyaes.AESModeOfOperationCTR(key)
  ctxt2 = base64.b64decode(ctxt_b64)
  dtxt_b64 = AES.decrypt(ctxt2)

  # Write deciphered image
  with open(out_path, "wb") as file:
    file.write(base64.b64decode(dtxt_b64))

  print("B64 PLAIN IMAGE:\n%r\n" % ptxt_b64)
  print("B64 CYPHERED IMAGE:\n%r\n" % ctxt_b64)
  print("B64 DECYPHERED IMAGE:\n%r\n" % dtxt_b64)

  print("B64 SHA256 IN PLAIN IMAGE:\n%r\n" % hashlib.sha256(open(in_path, "rb").read()).hexdigest())
  print("B64 SHA256 OUT DECIPHERED IMAGE:\n%r\n" % hashlib.sha256(open(out_path, "rb").read()).hexdigest())
  print("ARE EQUALS??: " + str(ptxt_b64 == dtxt_b64))
  assert(ptxt_b64 == dtxt_b64)

def get_random_key(mode):
  mode = int(mode)
  if mode not in [128, 192, 256]:
    print("'" + mode + "' mode does not exist")
    exit()
  return os.urandom(mode//8)

if __name__ == '__main__':
  main()