# H2
この問題は解けなかった問題．<br><br>
pcapファイルとgoファイルが渡される．pcapファイルを開くと100万以上のパケットがあり，この中からflagを探し出すようだ．goファイルの方をチェックすると，<br><br>
```
if r.URL.Path == SECRET_PATH {
      w.Header().Set("x-flag", "<secret>")
    }
w.WriteHeader(200)
fmt.Fprintf(w, "Can you find the flag?\n")
```
<br><br>
どうやら特定のリクエストパスに対しての応答のみ，ヘッダーのx-flagにflagを書き込んでいるようだ．なお，リクエストパスというのは下の画像の赤枠内の，/AABなどが該当する．<br><br>
<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/172322572-3c4f4b18-aea9-43e9-afab-ee594c8b31f7.png"><br><br>
このまま検索かけてもいいけど，明らかに100万パケットは多すぎるのでまずはステータスコードが200と書かれたhttp2ヘッダーパケットに絞り込む．フィルターの欄に<br>
`http2.headers.status eq 200`<br>
で，およそ4万パケットまで減らすことができる．そしたら，パケット検索機能(上の虫眼鏡アイコン)から，「詳細パケット」を選択肢，"x-flag"や"ctf4b"などで検索してみる．するとflagを見つけることができた．

<details>
<summary>H2の答え</summary>
ctf4b{http2_uses_HPACK_and_huffm4n_c0ding}<br><br>
<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/172766688-354842c6-103a-46fc-bd87-969eecaf7471.png">
</details>