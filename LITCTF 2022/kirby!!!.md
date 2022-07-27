# kirby!!!
解けなかった問題シリーズその２<br>
mp3ファイルの解析を行う問題．再生して聞いてみると明らかに最初の5秒くらいにノイズが追加されているのが分かる．残りはカービィのゲームbgm（素晴らしい曲）．とりあえず波形を確認するためにAudacityで開いてみる．<br><br>

<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181217430-8fb63c72-d86a-4a1b-9da9-7775d2e10013.png">
<br><br>
Audacity全く触ったこと無かったからインストールからここまでくるのに時間を取られた．ここから迷走してしまい，原曲との差分を取ればノイズ部分に何か見つかるんじゃね？とか考えてたけどどうやら違ったらしい．コンテスト終了後にdiscordのwriteupチャンネルに行くと，<br><br>

<img width="195" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181218694-b62910e0-50f2-4273-a0df-b3403df35960.png">
<br><br>
スペクトログラムという単語が．調べてみると，周波数スペクトルを計算し，グラフに反映したものを指すらしい．Audacityにもスペクトログラムの機能があるので使用してみるとこのようになった．<br><br>

<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181219317-9677321d-4e92-473b-917f-78ac5f4d972a.png"><br><br>
このように横軸を時間，縦軸を周波数，そして色の明るさが周波数強度を表している．これを見れば明らかだが，冒頭のノイズ部分に文字が見える．これがflagである．

<details>
<summary>答え</summary>
LITCTF{K1RBY1SCOOL!}<br><br>
<img width="274" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/181220114-0e822da1-d28a-4529-806b-2decea7a0176.png">
</details>