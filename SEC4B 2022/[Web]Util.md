# Util

この問題は解けなかった．writeupを見て実際に自分の手でflagを入手する所までやったのでここに残す．<br><br>

問題のwebページにアクセスすると，IPアドレスを入力することでpingコマンドを実行してくれるページが現れる．<br><br>
<img width="643" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/172041399-2a4402a5-3186-42a9-ac80-1ef467f5f5fd.png"><br><br>
まずはpingコマンドと併用してディレクトリ探索をしてflagの手がかりを得たいので，<br>
`127.0.0.1 | ls`<br>
と入力してみる．しかし「無効なIPアドレスです」と表示され，実行できなかった．そこでページのソースを表示してみると，41行目に
```
if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(address))
```
と書かれており，IPアドレス以外の入力が弾かれるようになっているようだ．この弾く仕組みはクライアント側のブラウザ上で行われているため，なんとか送信さえできれば目当ての情報は返ってきそう．<br><br>

そこで，Burp Suiteを使ってHTTPリクエストのPOSTメソッドを書き換えてみることにする．<br><br>
<img width="747" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/172041813-d1311bca-e032-4230-afe1-91eb4612e2c9.png">
<br><br>
本来のHTTPリクエストが左側で，応答が右側である．リクエスト内の緑色の文字で書かれたIPアドレスを，<br>
`"127.0.0.1 | ls"`<br>
のように書き換えて送信してあげると，<br><br>
<img width="751" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/172041839-ab71214a-e03e-457e-a627-4d2009d3d03e.png"><br><br>
このように，lsコマンドの結果を返してくれる．ここで，lsコマンドの結果が<br>
`api\npages\n`<br>
とあるが，間の'\n'は改行を表しているのでpathが繋がっているわけではないことに注意．<br><br>

lsコマンドの結果が得られることは分かったが，flagについてはまだ何も分かっていないのでもう少し探索してみる．次は<br>
`"127.0.0.1 | ls /"`<br>
と書き換えて再び送信．これはルートディレクトリ内を調べることになる．<br><br>
<img width="748" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/172041969-7c2b598a-5e33-48fb-a726-483d4e837e95.png"><br><br>
するとこのような結果に．flagらしきファイルflag_A74FIBkN9sELAjOc.txtが存在することが確認できた．<br>
`"127.0.0.1 | cat /flag_A74FIBkN9sELAjOc.txt"`<br>
を送信しflagが入手できた．
<details>
<summary>Utilの答え</summary>
ctf4b{al1_0vers_4re_i1l}<br><br>

<img width="742" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/172042105-d731a74e-d086-4d74-85aa-c381f1e8f834.png">

</details>