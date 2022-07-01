import string

cipher="ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

LOWERCASE_OFFSET = ord("a")	#Unicode番号へ変換(97 or 0x61)
ALPHABET = string.ascii_lowercase[:16]	#abcdefghijklmnopqrstuvwxyzの0~15文字(pまで)

char_list = string.ascii_letters   #小文字と大文字すべて
key = "a"    #-'a'でシフトする回数

#a~Zをb16_encに通した場合（つまりシフト0で暗号化した場合）
#for ch in char_list:
#    print(ch+": " + b16_encode(ch))

#最初がihになるのは，e(gf),v(hg),C(ed),T(fe)のどれか．シフト回数は2,1,4,3 -> keyはb,c,d,fを試す

x=""
for ch in cipher:
    x+= ALPHABET[ord(ch) - ord('c')]
#print(m)

#確認
m=""
for i in range(int(len(x)/2)):
    binary1 = "{0:04b}".format(ord(x[2*i])-ord('a'))
    binary2 = "{0:04b}".format(ord(x[2*i+1])-ord('a'))
    binary=binary1+binary2  #2進数の文字列
    m+=chr(int(binary,2))   #1文字に直して文字列に追加
print(m)