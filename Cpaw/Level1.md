# Level1- [Level1](#level1)
  - [Q1.\[Misc\] Test Problem](#q1)
  - [Q6.\[Crypto\] Classical Cipher](#q6)
  - [Q7.\[Reversing\] Can you execute ?](#q7)
  - [Q8.\[Misc\] Can you open this file ?](#q8)
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