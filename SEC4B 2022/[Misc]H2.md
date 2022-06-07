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
どうやら特定のリクエストパスに対しての応答のみ，ヘッダーのx-flagにflagを書き込んでいるようだ．なお，リクエストパスというのは下の画像の赤枠内の，/AABなどが該当する．br><br>
<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/172322572-3c4f4b18-aea9-43e9-afab-ee594c8b31f7.png"><br><br>
