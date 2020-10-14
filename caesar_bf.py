text = "bg max fhobx patm bl max gtfx matm tetg mnkbgz ztox mh max ftvabgx"
text = list(map(ord, list(text)))

def decrypt(text, i):
  plus_one = list(map(lambda c : (((c + i) - 97)%26) + 97, text))
  text = plus_one
  new = list(map(chr, plus_one))
  return "".join(new)

text = "rwgxhidewtg"
text = list(map(ord, list(text)))
for i in range(27):
  ptxt = decrypt(text, i)
  print(ptxt)

# ans = ["qgtpztg", "tcxvbp", "glvmwxstliv", "rwgxhidewtg"]
# for i in range(len(ans)):
#   print(decrypt(ans[i], 7))

# inutheumovieuwhatuisutheunameuthatualanuturingugaveutoutheumachine
# bg max fhobx patm bl max gtfx matm tetg mnkbgz ztox mh max ftvabgx
# in the movie what is the name that alan turing gave to the machine:
# christopher
# ~ caesar_7

# text = "christopher"
# text = list(map(ord, list(text)))
# encr = list(map(lambda c :chr((((c + 8) - 97)%26) + 97), text))
# print(encr)

print(len("rwgxhidewtg")) 
print(len("christopher")) 