# stonks(picoCTF2021より)
フォーマット文字列攻撃についての問題を初めて解いたので忘れないうちにここに残します．<br>
配布されたvuln.cを読んでみる，以下はbuy_stonks関数で，ところどころコメントもいれた．

```
//株を買う関数
int buy_stonks(Portfolio *p) {
	//(エラー時)
	if (!p) {
		return 1;
	}

	//ファイルfからflagをapi_bufに移す
	char api_buf[FLAG_BUFFER];
	FILE *f = fopen("api","r");
	if (!f) {
		printf("Flag file not found. Contact an admin.\n");
		exit(1);
	}
	fgets(api_buf, FLAG_BUFFER, f);

	//所持金，所有株を同期
	int money = p->money;
	int shares = 0;
	//一時記録用の株クラス
	Stonk *temp = NULL;

	//お金がある限り，ループ
	printf("Using patented AI algorithms to buy stonks\n");
	while (money > 0) {
		//1~maxの所持金の数だけsharesに代入
		shares = (rand() % money) + 1;
		//株を1つ定義し，tempに
		temp = pick_symbol_with_AI(shares);
		//もともと空のtempのnextにpのheadを代入
		temp->next = p->head;
		//pのheadにtempを代入
		p->head = temp;
		//shares分所持金を減らす
		money -= shares;
	}
	printf("Stonks chosen\n");

	// TODO: Figure out how to read token from file, for now just ask

	char *user_buf = malloc(300 + 1);
	printf("What is your API token?\n");
	scanf("%300s", user_buf);
	printf("Buying stonks with token:\n");
	//ここでなぜか入力した文字列を表示している．フォーマット文字列攻撃が使えそう．(%xとか)
	printf(user_buf);

	// TODO: Actually use key to interact with API

	view_portfolio(p);

	return 0;
}
```
<br>
ここで気になるのが，print(user_buf)で入力した文字列をわざわざ表示している点．ここがフォーマット文字列攻撃の脆弱性であると予想．<br>
FLAG_BUFFERにflagが格納されているはずなので，%xを連打して取り出そうと試みる．<br><br>

![キャプチャ](https://user-images.githubusercontent.com/64766627/170829477-f84bcd1e-a2fd-4e59-bf00-35a43a868db3.png)<br><br>

まとめてアスキー変換するとこんな感じに(CyberChefを利用)<br><br>
<img width="479" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/170829532-60ae8f50-d5d0-4709-9b14-4036c2e56a58.png"><br><br>

明らかにflagっぽい文字列が見つかるけど，リトルエンディアンなのか順番が少しだけおかしい．正しい順番で並べるように以下のプログラムを用意．（solvestonks.py）<br><br>

```
from ctypes import sizeof

sipher='ocip{FTC0l_I4_t5m_ll0m_y_y3n2fc10a10ÿý.}÷ùZø'
message=''
stack=[]
for i in range(len(sipher)):
    stack.append(sipher[i])
    if(i%4==3):
        for j in range(4):
            message+=stack[3-j]
            #print(message)
        stack=[]
print(message)
```

こんな感じのプログラムを組んで，flagを入手．}より後ろは必要なし．
```
picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}.ýÿøZù÷
```
