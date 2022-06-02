# Level3
- [Level3](#level3)
  - [Q23.\[Reversing\] またやらかした！](#q23reversing-またやらかした)

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