# Level1
- [Q1.\[Misc\] Test Problem](#q1misc-test-problem)
- [Q6.\[Crypto\] Classical Cipher](#q6crypto-classical-cipher)

## Q1.\[Misc\] Test Problem
チュートリアル  
問題文に書かれているものをそのままコピペするだけでクリア．以後cpaw{...}の形式で回答する． 
<details>
<summary>Q1のこたえ</summary>

cpaw{this_is_Cpaw_CTF}
</details> 

## Q6.\[Crypto\] Classical Cipher
暗号文: fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu} が与えられる．問題文を読むと，どうやら`シーザー暗号`が用いられているらしい．つまり暗号文を3文字分戻してあげれば答えが得られる．
解読できるwebサイトがあるので探してみるのが楽だしおすすめ．例えば[こことか](https://linesegment.web.fc2.com/application/cipher/Caesar.html)  
<details>
<summary>Q6のこたえ</summary>

cpaw{Caesar_cipher_is_classical_cipher}
</details> 

## Q7.\[Reversing\] Can you execute ?
拡張子のないファイルを渡され，どうにかして実行してFlagを入手したい．まずは，LinuxやUnix環境(Windowsの人はVMやSygwinを利用)でターミナルを開いて，`file`コマンドを使ってファイル形式を調べる．  
![Q7fileコマンド](https://user-images.githubusercontent.com/64766627/165731752-63fe55bd-f72f-4d41-ae8d-3ffef3637677.JPG)
するとこのように，`ELFファイル`であることが判明する．ELFファイルについて調べてみると，Linux環境で実行できるようだ，  
よって
<details>
<summary>Q6のこたえ</summary>

cpaw{Do_you_know_ELF_file?}
</details> 
