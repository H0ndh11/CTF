# math test
配布された実行ファイルを動かしてみると，次のような10個の質問に正解すればflagが手に入るようだ．ただし後半の問題は問題文から正解を導き出すのは不可能となっている．<br><br>
<img width="446" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181497516-937eba00-41d6-490d-b598-4975515e4c65.png"><br><br>

この問題ジャンルはrevなので，デバッガ(gdb)から実行してみる．main関数の中身を確認したいので，`b main`でブレークポイントをしかけ，`r`で実行．その後，`disas`で逆アセンブル結果を表示．<br><br>
<img width="444" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181499232-74222caa-cbd2-40bd-9f58-514424b96bda.png"><br><br>

探すべきポイントは，入力を受け付けて直後に分岐命令があるところである．というのも，回答入力後，正解不正解を判定していると予想されるからだ．...と思ったがどうやら回答入力直後には正解判定は無かった．その代わりに，ループ文の分岐命令のようなものが確認できた．<br><br>
<img width="446" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181500869-caf577b2-892d-45f9-8ea3-b8e111d15d68.png"><br><br>

上の画像の1行目(scanと書かれている)が入力を受け付ける命令となっていて，5行目にcmpで比較，6行目にその結果が0未満でmain+47へジャンプとなっている．main+47は既に通ってきたアドレスであり，手前に戻されることから質問と回答を10回繰り返してから正解判定を行っているのかな？そうなると次に確認すべきなのはループを抜けた後，すなわち8行目に書かれているgrade_test関数である．`b grade_test`でブレークポイントをしかけ，入力を一通り済ませる．後々入力結果が比較されたのを確認しやすいように，10個の質問の回答はすべて5とした．<br><br>
<img width="450" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181663780-a9f3b7d7-3181-4c7e-bc01-a5cad93ae7f2.png"><br><br>

`r`で実行後，cmp命令とjne命令が連続しているところまで進める．その前にcmp命令とjl命令が連続している場所があるが，これは正解判定ではなくループ条件の分岐なのでスルー．<br><br>
<img width="447" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181664092-dc2c954e-17c7-47a9-8737-9a3d3cd1be2a.png"><br><br>

grade_test+72にあった．ここではcmp命令でrdxとraxの値を比較し，一致するかしないかで分岐が行われている．つまりrdxとraxのどちらかに自分の入力結果の5が，もう片方に答えが格納されていると予測できる．実際にレジスタを確認すると<br><br>

~~~
RAX: 0x2 

RBX: 0x0 

RCX: 0x0 

RDX: 0x5 
~~~

このような結果であった．1つ目の質問内容からもRAXが解答で間違いなさそう．あとはこの作業を10回繰り返せば全ての質問の解答を得ることができる．各質問の答えは以下のようになった．これを10進数に戻して通常実行時に入力してflagを入手．

~~~
2
4
f0
3
9de8d6d
a
591587
6a11e49
2060e95f
9
~~~

<details>
<summary>答え</summary>
LITCTF{y0u_must_b3_gr8_@_m4th_i_th0ught_th4t_t3st_was_imp0ss1bl3!}
</details>