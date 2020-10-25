clc
#----------------------------------------------------
# Tests if coprimes_21 with multiplication modulo 21
# is a group
#----------------------------------------------------

# CLOSURE
coprimes_21 = [1, 2, 5, 8, 10, 11, 13, 16, 17, 19, 20]
flag = 0;
for i = coprimes_21
  for j = coprimes_21
    mult = mod(i*j, 21);
    if mult >= 21
      flag = 1;
    endif
  endfor
endfor
flag

# ASSOC
flag = 0;
for i = coprimes_21
  for j = coprimes_21
    for k = coprimes_21
      temp = mod(i*j, 21);
      res1 = mod(temp*k, 21);
      
      temp = mod(j*k, 21);
      res2 = mod(i*temp, 21);
      
      if (res1 != res2)
        printf("Non associativity!")
        flag = 1
      endif
    endfor
  endfor
endfor
flag

# IDENTITY
flag = 0;
for i = coprimes_21
  subflag = 0;
  for j = coprimes_21
    res = mod(i*j, 21);
    if (res == 1)
      subflag = 1;
      break;
    endif
  endfor
  if (subflag == 0)
    break;
  endif
endfor
flag

# IDENTITY
flag = 0;
identity = -1;
for i = coprimes_21
  id_ok = 0
  ctr = 0
  for j = coprimes_21
    res1 = mod(i*j, 21)
    res2 = mod(j*i, 21)
    if (res1 != j)
      break;
    endif
    ctr += 1;
  endfor
  if (size(coprimes_21)(1) != ctr)
    identity = i;
  endif
endfor
identity
