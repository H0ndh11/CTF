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

(以下工事中)