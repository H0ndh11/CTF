# Running Up That Hill
解けなかった問題シリーズその１<br>
次のテキストファイルから暗号解読を行う

~~~
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}

5 19 27
10 19 24
11 6 16

A8FC7A{H7_ZODCEND_8F_CCQV_RTTVHD}
~~~

これ見てさっぱり分からなかったが，コンテスト終了後にdiscordを覗きに行くとどうやらhill sipherと呼ばれる暗号方式があるみたいだ．テキストファイル1行目の'A'～'}'を0～38とし，行列の積とmod39を用いて計算すればflagが入手できそう．逆行列求めるのもコード書くのも面倒なので[ここ](https://www.dcode.fr/hill-cipher)で自動復号．なんて便利なんだ...

<details>
<summary>答え</summary>
LITCTF{B3_RUNN1NG_UP_TH4T_H1LLLL}
</details>