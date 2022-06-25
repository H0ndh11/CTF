# Level3
- [Level3](#level3)
  - [Q23.\[Reversing\] またやらかした！](#q23reversing-またやらかした)
  - [Q24.\[Web\] Baby's SQLi - Stage 2 -](#q24web-babys-sqli---stage-2--)
  - [Q26.\[PPC\] Remainder theorem](#q26ppc-remainder-theorem)

---
<br><br>

## Q23.\[Reversing\] またやらかした！
またまたflagを出力する関数を書き忘れた実行ファイルが渡された．まずは`file rev200`でファイルフォーマット確認すると，elfファイルであることが分かった．実行してみても，とくに何も出力されないようだ．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/171559446-5183b9ae-98c8-41d4-ab3f-c78f10b1f743.png)<br><br>
Ghidraを使って逆アセンブル&逆コンパイルしてみる．<br><br>
<img width="432" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/171559854-0406d840-7fb8-4a1b-ad79-bb33ae47aaf7.png"><br><br>
メイン関数はこんな感じ．少しだけ分かりやすく書き換えていくと<br><br>
<img width="440" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/171561792-d0f60c4c-9522-4476-baf8-80ebbdf3265a.png"><br><br>
stringに格納されている文字列を1文字づつ，00011001と排他的論理和をとり，文字列化したものが最終的にlocal_44になる．local_44を求めてあげると正解であるflagを手に入れることができた．
<details>
<summary>Q23のこたえ</summary>

cpaw{vernam!!}
</details> 

---
<br><br>

## Q24.\[Web\] Baby's SQLi - Stage 2 -
Level2のQ22から，Stage2に進むためのurlを入手しているので，まずはそのページにアクセス．するとログイン認証を突破できればflagが手に入ることがわかる．まずはログイン認証問題の定番で，ユーザー名pristeruの後ろに文字列終了の'とコメントアウトの--を追加し，`prisuteru'--`とし，パスワードには適当な文字をいれてみる．<br><br>
<img width="623" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/171566058-ab8052fb-54a6-4aed-99e5-eeb1137c8e66.png"><br><br>
なんとたったこれだけで突破することができた．一応原理としては，本来ならば<br>
`SELECT * FROM users WHERE username = 'porisuteru' AND password = '本来のパスワード'`<br>
というクエリを送信し，usernameとpasswordが一致するデータを返すようになっている．しかし，今回入力した結果<br>
`SELECT * FROM users WHERE username = 'porisuteru'--' AND password = 'abc'`<br>
というクエリが生成されてしまう．これにより--より後ろはコメントアウト，すなわち処理側が無視する文字列となってしまい，usernameのみ一致すればログインできてしまうということになるのだ．

<details>
<summary>Q24のこたえ</summary>

cpaw{p@ll0c_1n_j@1l3:)}
</details> 

---
<br><br>

## Q26.\[PPC\] Remainder theorem
次の数式を解く問題<br><br>
~~~
x ≡ 32134 (mod 1584891)
x ≡ 193127 (mod 3438478)

x = ?
~~~
<br>
問題文にPPCと書かれているように，この問題はプログラムを組んで解決するのが良さそうだ．やることはシンプルで，最初に<br><br>

~~~
x ≡ 32134 (mod 1584891)
~~~
<br>
を満たすxを列挙していき，<br><br>

~~~
x % 3438478 = 193127
~~~
<br>
が成り立つか確認していけばよい．ただし，xの桁数が大きくなることが予想されるので型宣言に気を付ける．自分は次のようなコードを書いた．（同ディレクトリ内のq26.cと内容は同じ）<br><br>

~~~
#include <stdio.h>

int main(void){
    long long int x=0,i;
    for(i=0;;i++){
        x = i * 1584891 + 32134;
        //printf("%lld\n",x); //確認用
        if(x % 3438478 == 193127){
            printf("%lld\n",x);
            printf("result %% 1584891: %lld\n", x%1584891);
            printf("result %% 3438478: %lld\n", x%3438478);
            break;
        }
    }
}
~~~
<br>
これをコンパイルし<br><br>

~~~
gcc -o q26 q26.c
~~~
<br>
実行すればxの値が求まる．（コンパイル済の実行ファイルは同ディレクトリのq26.exe）