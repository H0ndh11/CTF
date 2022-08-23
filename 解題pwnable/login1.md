# login1
バッファオーバーフロー問題１．サーバで動いている実行ファイルのソースコードの中で，main関数に注目する．

~~~
int main()
{
    char id[0x20] = "";
    char password[0x20] = "";
    int ok = 0;

    setup();

    printf("ID: ");
    gets(id);
    printf("Password: ");
    gets(password);

    if (strcmp(id, "admin") == 0 &&
        strcmp(password, flag) == 0)
        ok = 1;

    if (ok) {
        printf("Login Succeeded\n");
        printf("The flag is: %s\n", flag);
    } else
        printf("Invalid ID or password\n");
}
~~~

早速IDの値が`admin`であることがわかる．また，入力を受け付ける際にgets関数が使われており，変数のサイズを超過して入力ができてしまうという脆弱性がある．これを用いてバッファオーバーフローをしかけ，変数okの値を0以外の値に書き換えられれば分岐命令を突破してflagが手に入るという算段だ．現時点でスタック内の状態を予想するとこんな感じだろうか．<br><br>

![スクリーンショット](https://user-images.githubusercontent.com/64766627/186165836-93ed73ef-a840-48e7-b969-2fbe88e5dbb1.png)<br><br>

宣言した順番に積まれると思ってこう考えたが，もし本当にこの順番で積まれているのであればokの書き換えはできなそうなので，実際は違うだろう．なのでgdbにて調査をする．<br><br>

![スクリーンショット2](https://user-images.githubusercontent.com/64766627/186168422-c07fdb44-7d88-4175-b4fb-3de031ecc4b1.png)<br><br>

少しわかりにくいが，上の画像がokが0であるかどうかを比較するcmp命令の直前である．ここからokが`rbp-0x4`に格納されていることが確認できる．この画像には移っていないが，`rbp=0x7fffffffdf60`であることから，IDやpasswordが格納されている位置との関係を整理すると，以下のような構造であることが判明する．<br><br>

![スクリーンショット3](https://user-images.githubusercontent.com/64766627/186170324-8acc2783-4344-45bb-8416-85f4b18bdf19.png)<br><br>

okとidの間が何なのかはまだよくわかっていないけど，スタックに積まれる順番に関しては宣言順にはならなかった．ちょっとだけ調べてみたところ，積まれる順番に関してはルールはなく，規則性もあまり期待できないので問題に応じて毎回確認するのがよさそう．とはいえここまで丁寧に確認する必要はないかもしれないが．

あとは，idを45文字以上(0x2C+1)入力するか，passwordを77文字以上入力すればokの値が書き換わり，flagを入手することができる．
