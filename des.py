import pyDes
import base64
import sys
import hashlib

key = "JUANCAMI"
in_path = sys.argv[1]
out_path = sys.argv[2]

# Open plain image
with open(in_path, "rb") as file:
  img_in = bytearray(file.read())

DES = pyDes.des(key, pyDes.ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

ptxt = base64.b64encode(img_in)
ctxt = base64.b64encode(DES.encrypt(img_in))
dtxt = base64.b64encode(DES.decrypt(base64.b64decode(ctxt)))

# Write deciphered image
with open(out_path, "wb") as file:
  img_out = file.write(base64.b64decode(dtxt))

print("B64 PLAIN IMAGE:\n%r\n" % ptxt)
print("B64 CYPHERED IMAGE:\n%r\n" % ctxt)
print("B64 DECYPHERED IMAGE:\n%r\n" % dtxt)

print("B64 SHA256 IN PLAIN IMAGE:\n%r\n" % hashlib.sha256(open(in_path, "rb").read()).hexdigest())
print("B64 SHA256 OUT DECIPHERED IMAGE:\n%r\n" % hashlib.sha256(open(out_path, "rb").read()).hexdigest())
print("ARE EQUALS??: " + str(ptxt == dtxt))
assert(ptxt == dtxt)
