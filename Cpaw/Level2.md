# Level2
- [Level2](#level2)
  - [Q13.\[Stego\] 隠されたフラグ](#q13stego-隠されたフラグ)
  - [Q15.\[Web\] Redirect](#q15web-redirect)
  - [Q16.\[Network+Forensic\] HTTP](#q16networkforensic-http)
  
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
ポップアップが表示されるのですべて保存をクリック．