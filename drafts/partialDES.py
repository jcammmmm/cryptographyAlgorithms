def main():
  str_R6 = "11101001011001111100110101101001"
  str_K6 = "011000111010010100111110010100000111101100101111"
  assert(len(str_R6) == 32)
  assert(len(str_K6) == 48)

  K6 = to_bool_arr(str_K6)
  R6 = to_bool_arr(str_R6)
  print(R6)
  print(K6)



def to_bool_arr(str):
  return list(map(int, list(str)))

if __name__ == "__main__":
  main()
  