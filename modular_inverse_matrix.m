clc
clear
A = [261 286; 182 131];
K = [11 8; 3 7];
m1 = [9 20];
m2 = [11 24];
c1 = mod(m1*K, 26);
c2 = mod(m2*K, 26);
c1
c2
c = [c1 c2]
letters = char(c + 65)