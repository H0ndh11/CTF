# phisher
問題文に書かれている通りホモグラフ攻撃を体験する問題だ．まずは指定されたドメイン・ポートにアクセスする．すると何やら入力ができるみたいで，適当な文字列を並べてみる．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/172049614-8cf45503-dfe9-4012-8a4c-5c1e811a0a09.png)<br><br>
"www.example.com"じゃないといけないらしい．ホモグラフ攻撃は，偽のurlを本物とよく似た文字を使う攻撃なので，"www.example.com"を別の文字で表現するのかなと予想．ひとまず"www.example.com"をそのまま入力してみる．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/172049751-2503102a-f0b1-4577-aee4-8df1bf465937.png)<br><br>
「wが含まれています」という結果が帰ってきた．wっぽくてwじゃないωを使ってみると<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/172049806-4555d3b3-3e0c-4225-943e-7a2acaf1cf57.png)<br><br>
次はピリオド．という感じに頭から他の文字に置き換えていく．<br><br>
本当はフォントを配布ファイルから推測しながら入力していくみたいだけど，大会期間中はそこまで頭が回らなかったのでブルートフォース的にいろんな文字を1文字ずつ試した．その結果，`ωωω․ехаⅿρIе․ⅽο㎜`でなんとかクリアすることができた．
<details>
<summary>phisherの答え</summary>
ctf4b{n16h7_ph15h1n6_15_600d}<br><br>

![キャプチャ](https://user-images.githubusercontent.com/64766627/172052511-6e138ebc-f876-4ebc-b49b-b2aaca5112ca.png)

</details>