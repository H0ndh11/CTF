from random import shuffle

flag = b"ctf4b{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"

cipher = []

for i in range(len(flag)):
    f = flag[i]
    #iを加え，2乗し，iを加える．
    #cならば，(99+0)**2+0=9801
    c = (f + i)**2 + i
    cipher.append(c)

#リスト内をシャッフル
shuffle(cipher)
print("cipher =", cipher)

cipher = [12147, 20481, 7073, 10408, 26615, 19066, 19363, 10852, 11705, 17445, 3028, 10640, 10623, 13243, 5789, 17436, 12348, 10818, 15891, 2818, 13690, 11671, 6410, 16649, 15905, 22240, 7096, 9801, 6090, 9624, 16660, 18531, 22533, 24381, 14909, 17705, 16389, 21346, 19626, 29977, 23452, 14895, 17452, 17733, 22235, 24687, 15649, 21941, 11472]

#リストの初期化
message=[]
for i in range(49):
    message.append("0")

for num in cipher:
    #jはループ番号
    j=30
    #indexはnumと2乗値の差が最小となるときの値が格納される
    index=10000
    while(j<200):
        m=num-j**2
        #より差が小さいなら更新
        if(index>m and m>=0):
            index=m
            ch=j-index
        j+=1
    print(str(num) + " = (" + str(ch) + " + " + str(index) + ")の2乗 + " + str(index) + "   つまりflagの" + str(index) + "番目の文字は" + chr(ch))
    message[index]=chr(ch)

for char in message:
    print(char, end='')