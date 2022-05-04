# Level1- [Level1](#level1)
  - [Q1.\[Misc\] Test Problem](#q1)
  - [Q6.\[Crypto\] Classical Cipher](#q6)
  - [Q7.\[Reversing\] Can you execute ?](#q7)
  - [Q8.\[Misc\] Can you open this file ?](#q8)
  - [Q9.\[Web\] HTML Page](#q9)
  - [Q10.\[Forensics\] River](#q10)
---
<br><br>
<a id="q1"></a>

## Q1.\[Misc\] Test Problem
チュートリアル  
問題文に書かれているものをそのままコピペするだけでクリア．以後cpaw{...}の形式で回答する． 
<details>
<summary>Q1のこたえ</summary>

cpaw{this_is_Cpaw_CTF}
</details> 

---
<br><br>
<a id="q6"></a>

## Q6.\[Crypto\] Classical Cipher
暗号文: fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu} が与えられる．問題文を読むと，どうやら**シーザー暗号**が用いられているらしい．つまり暗号文を3文字分ずらしてあげれば答えが得られる．
解読できるwebサイトがあるので探してみるのが楽だしおすすめ．例えば[こことか](https://linesegment.web.fc2.com/application/cipher/Caesar.html)  
<details>
<summary>Q6のこたえ</summary>

cpaw{Caesar_cipher_is_classical_cipher}
</details> 

---
<br><br>
<a id="q7"></a>

## Q7.\[Reversing\] Can you execute ?
拡張子のないファイルを渡され，どうにかして実行してFlagを入手したい．まずは，LinuxやUnix環境(Windowsの人はVirtualBoxやSygwinを利用)でターミナルを開いて，**file**コマンドを使ってファイル形式を調べる．
<br><br>
![Q7fileコマンド](https://user-images.githubusercontent.com/64766627/165731752-63fe55bd-f72f-4d41-ae8d-3ffef3637677.JPG)
<br><br>
するとこのように，**ELFファイル**であることが判明する．ELFファイルについて調べてみると，windowsにおけるexeファイルような立ち位置で，Linux環境で実行できるファイルのようだ，  
よって，Linuxターミナルで`./exec_me`と打つだけで実行され，Flagが得られる．

<details>
<summary>Q7のこたえ</summary>

cpaw{Do_you_know_ELF_file?}
</details> 

---
<br><br>

<a id="q8"></a>

## Q8.\[Misc\] Can you open this file ?
拡張子のないファイルを渡されたためどのソフトウェアで開けばいいのかわからない．この問題もQ7同様に，まずはlinux or Unixで`file open_me`を打ってみる．
<br><br>
![Q8fileコマンド](https://user-images.githubusercontent.com/64766627/166086311-ffcafdd2-d0c0-439c-9521-04a0d0a750d9.JPG)
<br><br>
すると，3行目あたりにMicrosoft Office Wordという文字列が確認できるので，Wordで開いてFlag入手．Windowsなら<br>
ファイル右クリック->プログラムから開く->Word選択<br>
で開くことができる．

<details>
<summary>Q8のこたえ</summary>

cpaw{Th1s_f1le_c0uld_be_0p3n3d}
</details> 

---
<br><br>

<a id="q9"></a>

## Q9.\[Web\] HTML Page
Webサイトからフラグを探す問題．親切にもHTMLについての説明がされているので，対象のWebサイトに飛んだら<br>
右クリック->ページのソースを表示<br>
からHTMLを確認する．この中のどこかにFlagがあるので探す．面倒なら**ctrl + F** でページ内検索できるのでcpawと入力すれば一瞬で見つかる．

<details>
<summary>Q9のこたえ</summary>

cpaw{9216ddf84851f15a46662eb04759d2bebacac666}<br><br>flagの中身が全て16進数で書かれてるから，ASCIIとかでメッセージが隠されてるのかなって思ったけど解読できない...<br>
特に意味はないのだろうか？
</details> 

---
<br><br>

<a id="q10"></a>

## Q10.\[Forensics\] River
川の景色が記録されているjpgファイルから川の名前を特定する問題．まずはダウンロードしてプロパティからファイルの情報を確認してみる．
<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/166688331-8fa06092-1919-4723-b713-909356f25cf4.JPG)
<br><br>
詳細タブにGPS情報が載っていることを確認．これを元にグーグルマップから検索をかける．（入力フォーマットに気を付ける）
<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/166699814-217e0413-ef6f-42bb-8eb1-fcb310c05aa8.JPG)
<br><br>
**甲突川**と呼ばれる川であることが判明．念のためストリートビューを確認してみるとさらに確信が得られる．建物とかは少しかわってるかもね．

<details>
<summary>Q10のこたえ</summary>

cpaw{koutsukigawa}<br><br>kotsukigawaじゃないので注意
</details> 

---
<br><br>