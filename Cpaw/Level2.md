# Level2
- [Level2](#level2)
  - [Q13.\[Stego\] 隠されたフラグ](#q13stego-隠されたフラグ)
  - [Q15.\[Web\] Redirect](#q15web-redirect)
  - [Q16.\[Network+Forensic\] HTTP](#q16networkforensic-http)
  - [Q17.\[Recon\] Who am I ?](#q17recon-who-am-i-)
  - [Q18.\[Forensic\] leaf in forest](#q18forensic-leaf-in-forest)
  - [Q19.\[Misc\] Image!](#q19misc-image)
  - [Q20.\[Crypto\] Block Cipher](#q20crypto-block-cipher)
  - [Q21.[Reversing] reversing easy!](#q21reversing-reversing-easy)
  
---
<br><br>

## Q13.\[Stego\] 隠されたフラグ
次のグラフのFlagが隠されているそうだ<br><br>
![steg10](https://user-images.githubusercontent.com/64766627/167430968-ed5b2eb3-3f5b-4091-b10a-554d6eeebd77.jpg)<br><br>
画像の左上の右下をよく見ると汚れみたいなのが付いてるので，拡大してみる．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/167431265-7273647b-18f6-45f6-8ed0-b6489a0daef6.JPG)<br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/167431704-de8cf2dd-0ebc-49c8-bdf7-065356e9e74c.JPG)<br><br>
察しのいい方ならもう気づいたかもしれないが，この記号の列は**モールス信号**を表している．これらを英字の列に直してあげると，Flagが手に入る．
<details>
<summary>Q13のこたえ</summary>

cpaw{hidden_message:)}<br><br>問題文に書かれている通り回答は小文字で．cpawは括弧の外にあるので省略
</details> 

---
<br><br>

## Q15.\[Web\] Redirect
渡されたURLにアクセスすると，リダイレクトされてクリックしたはずのURLと異なるページに飛ばされる．リダイレクトの様子を確認するために，URLをクリックする前に(chromeなら)画面上で<br>右クリック->検証<br>
でデベロッパーツールを開く．そしてネットワークタブを開く．そしたら次のような画面になるはず．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/167562372-ea01e58c-53bc-4e11-9465-7acc6a029d34.JPG)<br><br>
この画面が表示できたら，問題に書かれているURLをクリックしてみよう．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/167562796-1a094d9f-cc1c-47fc-b020-3632a56ba6bc.JPG)<br><br>
このように，ネットワークアクティビティに受け取ったデータがいくつか表示されている．最初に受け取ったq15.ctf.cpaw.siteを確認してみる．<br><br>
![tempsnip](https://user-images.githubusercontent.com/64766627/167563481-3bbeb4e8-f356-4a65-b9ed-ded8f861a478.png)<br><br>
なんとヘッダーにFlagが載っていた．

<details>
<summary>Q15のこたえ</summary>

cpaw{4re_y0u_1ook1ng_http_h3ader?}<br><br>
ステータスコード:302はリダイレクト，すなわちユーザーが取得しようとしたページが一時的に別の場所に移されていることを示している．
</details> 

---
<br><br>

## Q16.\[Network+Forensic\] HTTP
Wireshark必須．pcapファイルからページを復元する問題．ひとまず開いてみよう．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/167654313-be2fcb5f-0f11-4a57-9acb-377758f9d859.JPG)<br><br>
とにかくパケットが多い．でもWiresharkならHTTPパケットからWebページを復元してくれる超便利な機能があるので安心だね．<br><br>
<img width="960" alt="tempsnip" src="https://user-images.githubusercontent.com/64766627/167655295-b6a3401e-f564-415e-81b3-7cca4629fe4f.png"><br><br>
ポップアップが表示されるのですべて保存をクリック．これにより閲覧していたであろうWebぺージを見るためのデータが全て手に入った．htmlファイルを開いてみよう．2つあるが，どちらかを開くと以下の画面が表示され，ボタンを押せばFlagが手に入る．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/168066248-384d0400-ccea-48e7-9d47-e54de6903ece.JPG)<br><br>

<details>
<summary>Q16のこたえ</summary>

cpaw{Y0u_r3st0r3d_7his_p4ge}
</details>

---
<br><br>

## Q17.\[Recon\] Who am I ?
twitterで検索するのも一苦労なので，google検索しちゃおう．アカウント名とスペシャルフォース2というキーワードが入っていれば上の方に出てくるはず．

<details>
<summary>Q17のこたえ</summary>

cpaw{parock}
</details>

---
<br><br>

## Q18.\[Forensic\] leaf in forest
ファイルの中からFlagを探す問題．まずはいつも通りfileコマンドでフォーマットを調べてみると，どうやらpcapファイルらしい．Wiresharkで開くと，エラーが出て開けない．そこで，`string`コマンドを試してみる．(メモ帳で開くこともできるみたい)<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/168524689-266d8f36-4647-4032-8ae1-01b0c0e7b8e4.png)<br><br>
すると同じような文字列が大量に表示される．良く見てみると大文字がいくつか見つかるので，まずは邪魔な単語を消していく．メモ帳でやると楽．linuxターミナルでやるなら<br>
`sed -i s/love//g misc100`<br>
`sed -i s/live//g misc100`<br>
`sed -i s/\!//g misc100`<br>
loveとliveと!を消すと大分スッキリする．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/168527409-990a8bc2-2dce-4669-99c2-c02686bb0b44.png)
ここまでやって気づいたけど，小文字は全部消してよさそう．するとこんな感じに<br>
CCCPPPAAAWWW{{{MMMGGGRRREEEPPP}}}<br>
Flagの形式的に，全て小文字でcpaw{...}となるはずなので，小文字変換して重複を消すとFlagゲット
<details>
<summary>Q18のこたえ</summary>

cpaw{mgrep}
</details>

---
<br><br>

## Q19.\[Misc\] Image!
またまたファイルからflagを探す問題．解凍してみるとフォルダやらxmlのファイルやらが出てくる．一つだけ拡張子のないmymetypeというファイルがあるので，メモ帳で開いてみる．<br><br>
<img width="527" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/170498287-bd1920d6-3c16-4620-9471-3d9fb9ded780.png"><br><br>
調べてみたらオープンドキュメントというワードでで引っかかった．どうやらzipの状態で拡張子をodtに変更し，LibraOfficeで開けるらしい．けどなぜか俺のkalilinuxではLibraOfficeで開けなかった．もうすこし調べてみると，Word上でも開けることが分かった．なんか実際の画像とは異なるんだろうけど，これでFlagが入手できた．
<details>
<summary>Q19のこたえ</summary>

It_is_fun__isn't_it?<br>
LibraOfficeで開けなかったのは[これ](https://niszet.hatenablog.com/entry/2020/09/03/083000)が原因かも
</details>

---
<br><br>

## Q20.\[Crypto\] Block Cipher
暗号解読の問題．まずは与えられたc言語ファイルを見てみる．<br><br>
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char* argv[]){
  int i;
  int j;
  int key = atoi(argv[2]);
  const char* flag = argv[1];
  printf("cpaw{");
  for(i = key - 1; i <= strlen(flag); i+=key) for(j = i; j>= i - key + 1; j--) printf("%c", flag[j]);
  printf("}");
  return 0;
}
```
<br><br>
引数1に暗号文`ruoYced_ehpigniriks_i_llrg_stae`を，引数2に鍵となる数値を入力することで解読してくれるプログラムのようだ．さらに，for文からiは暗号文の長さ(31)まで，keyの値分増えながらループするようだ．この時点で，keyは1~32の範囲内であることが推測できる．よって次のようにコードを改変する．<br><br>
```
// crypto100ex.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char* argv[]){
  int i;
  int j;
  int key;
  //int key = atoi(argv[2]);	//引数2（数字）を文字列から数値への変換
  const char* flag = argv[1];	//flagに引数1（暗号文）を代入
  /*つまり
  crypto100.exe 暗号文 鍵
  で解読するイメージ
  */
  for(key=1;key<=32;key++){
    printf("cpaw{");
    /*
    i=key-1 から i=暗号文の長さ(31) までiを増やしながらループ
      j=i から j=i-key+1 までjを減らしながらループ
        j番目のflag文字列を出力
    */
    for(i = key - 1; i <= strlen(flag); i+=key) for(j = i; j>= i - key + 1; j--) printf("%c", flag[j]);
    printf("}\n");
  }
  return 0;
}

```
<br><br>
`gcc crypto100ex.c -o crypto100`でコンパイルして，ターミナル上で`crypto100.exe ruoYced_ehpigniriks_i_llrg_stae`と実行すると
```
cpaw{ruoYced_ehpigniriks_i_llrg_stae}
cpaw{urYoec_dheipngriki_s_illgrs_ate}
cpaw{ourecYe_diphingkiri_sll__grats}
cpaw{Your_deciphering_skill_is_great}
cpaw{cYourhe_deingip_skirrll_iats_g}
              ：
            (省略)
```
このように，4番目に意味のある英文が現れる．
<details>
<summary>Q20のこたえ</summary>

cpaw{Your_deciphering_skill_is_great}
</details>

---
<br><br>
## Q21.[Reversing] reversing easy!
flagを出力する関数を書き忘れた実行ファイルを渡された．とりあえずファイルのフォーマット確認と実行をやってみる．<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/171184479-692f24ab-7e8e-4359-8168-862691161e1e.png)<br><br>
当然これだけでflagは手に入らないが，cpaw{}は出力してくれているみたいだ．ここでGhidraをつかって逆コンパイル，逆アセンブルを試してみる．<br><br>
<img width="955" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/171186984-af1c086a-ba65-4fb6-a9ab-84447771da38.png">
<br><br>

main関数の逆コンパイル画面はキャプチャ画面右に表示される．本当は画面真ん中のアセンブリ言語読んで解析できるようになるといいんだけど，今回はc言語の方を見ます(わかりやすいし)．画像の赤枠内を確認すると，if文内が実行されていないことが分かる．つまり，if文内のputcharで合計9文字分出力されていればflagは完成となるのではないかと予想できる．しかし，9文字の文字列が格納されているであろうlocal_40は，4文字の文字列となっている．つまり，逆コンパイルがうまくいっていないことがわかるので，逆アセンブル画面のスタックも確認する．<br><br>
<img width="441" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/171189320-e3e7a603-ade5-40f4-9aa9-af2490cf99dd.png"><br><br>
local_40から9文字分なので，local_20までで，`79 61 6b 69 6e 69 6b 75 21`<br>
アスキー文字に変換すると，`yakiniku!`
あとはcpaw{}で囲めばクリア
<details>
<summary>Q21のこたえ</summary>

cpaw{yakiniku!}
</details>

---
<br><br>