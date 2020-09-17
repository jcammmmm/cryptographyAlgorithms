package com.clarocol.serviceAvailability.util;

public class Crypt {
  public static void main1(String[] args) {
    // String ss = "WKLVL VHAWU HPHOB LQVHF XUHHQ FUBSW LRQGR QRWXV HLWWR SURWH FWYDO XDEOH LQIRU PDWLR Q"; // k = 3 Caesar's Cipher
    String ss = "VSGUR AFNUN FGVZR GBERN QZLRZ NVYVJ VFUGU RLFRA QZRNO YBBQLR"; // k = 13 Rot13 Cipher
    int k = 13;

    for(char c : ss.toCharArray()) {
      int n = c;
      n -= 65;
      
      if (c == ' ') {
        System.out.print(" "); 
        continue;
      }
      int d = n - k;
      if (d < 0)
        d += 26;

      d += 65;
      System.out.print((char) d);
    }
  }

  public static void main2(String[] args) {
    System.out.println(41 % 7);
    System.out.println(-41 % 7);
  }

  public static void main(String[] args) {
    final int alphaSize = 26;
    char[][] tab = new char[26][26];
    for(int i = 0; i < alphaSize; i++) {
      for(int j = 0; j < alphaSize; j++) {
        int k = i + j;
        if (k >= alphaSize)
          k %= 26;
          tab[i][j] = (char) ( i + j);
          
        System.out.print(tab[i][j]);
      }
      System.out.println();
    }

  }
  /*
  THE REI SAS ECR ET
  CRY PTO CRY PTO CR
--------------------
  VYC GXW VRQ TVF GK
  */
}
