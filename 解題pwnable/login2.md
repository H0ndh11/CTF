# login2
バッファオーバーフロー問題２．１と同じようにまずはmain関数を見てみる．

~~~
int main()
{
    char id[0x20] = "";
    char password[0x20] = "";

    setup();

    printf("ID: ");
    gets(id);
    printf("Password: ");
    gets(password);

    if (strcmp(id, "admin") == 0 &&
        strcmp(password, flag) == 0) {
        printf("Login Succeeded\n");
        printf("The flag is: %s\n", flag);
    } else
        printf("Invalid ID or password\n");
}
~~~

今度はint型の変数okが無く，if文の分岐でidとpasswordの比較が行われている．ではどうやってこの認証を突破し，flagを表示させるかという話になってくる．その前に，前回と同じようにスタックの中身について書き出してみる．<br><br>

![スクリーンショット](https://user-images.githubusercontent.com/64766627/186422895-5885618a-6e3d-4f1f-8b55-2712f37bc058.png)<br><br>

ここで，idまたはpasswordを指定された長さを超えて入力し，rbp+0x8にmain関数後に帰るアドレスをflagを表示させる命令が書かれたアドレスに指定した場合について考える．認証失敗後，main関数が終了するタイミングで再びmain関数内に戻りflagを表示させることができる．つまり，idであれば適当な長さ40の文字列に加え，flagを表示させる命令があるアドレスを入力してあげればよい．<br><br>

![スクリーンショット2](https://user-images.githubusercontent.com/64766627/186425413-b98e26ab-c3d2-4a6b-8c95-1c9af29c7cf0.png)
<br><br>

では，書き換えるアドレスを探す，gdb内で`disass main`を用いてアセンブリ命令を表示する．今回の場合文字列比較strcmp,test,jneが2回ずつ行われた後がflag表示の処理なので，上の画像から0x401346ということになる．

これで入力内容は決まったが，あと一つ注意点として，アドレスを入力する場合，そのままでは数値として受け取られてしまうためアスキーコードに直す必要がある．しかし中には印字不可能な文字，非ASCII文字が含まれるため，少しだけ工夫する必要がある．pythonでスクリプトを書いたり，echoコマンドを用いたり，方法は色々あると思うが今回はバイナリエディターのstrilingを用いて以下のファイルを作成した．<br><br>

![スクリーンショット3](https://user-images.githubusercontent.com/64766627/186427396-d2badd50-26c6-4793-a857-a0c39b5fb98c.png)<br><br>

idには40文字のaに加え，リトルエンディアンでのアドレス，改行を示す0Aを挟んでpasswordに4文字のa，改行という内容だ．

あとはこれを問題サーバに送り付ければflagが手に入る．その際は以下のコマンドを使う．

`cat attack_login2.bin | nc localaddress 10002`

これはバイナリファイルを表示する際の内容をそのまま問題サーバに送るという意味である．これで解決．
