# gallery
これも時間内に解けなかった問題．<br>
問題のページを訪れると，slackとかで使えそうな文字スタンプが様々なファイル拡張子で並べられている．<br><br>
<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/174060847-4b64ac99-4399-48cb-b84d-d41e00ddebbf.png"><br><br>
例えばjpegを選べば，jpegファイルのスタンプが2つ表示された．画面上部のURLを見ると，<br>
`https://gallery.quals.beginners.seccon.jp/?file_extension=jpeg`<br>
と，末尾で拡張子を指定しているようだ．ここにいろんな拡張子をいれてみると，<br><br>
<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/174061298-74ba2259-34ed-4f44-889b-4c48ad6822e4.png"><br><br>
pdfでflagファイルらしきものが表示された．しかし開いてみると<br><br>
<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/174061444-d3fe82de-4b66-4301-9e62-79d7563ff633.png"><br><br>
このように?が羅列されていて，flagと思われる情報は見つからない．そこで，配布されたソースファイルの`main.go`を確認してみると<br><br>
~~~
func middleware() func(http.Handler) http.Handler {
	return func(h http.Handler) http.Handler {
		return http.HandlerFunc(func(rw http.ResponseWriter, r *http.Request) {
			h.ServeHTTP(&MyResponseWriter{
				ResponseWriter: rw,
				lengthLimit:    10240, // SUPER SECURE THRESHOLD 10240byteを超えたら送信しないようになっている
			}, r)
		})
	}
}
~~~
<br><br>
レスポンスでサイズ上限が設定されていた．BurpSuiteの方でも確認してあげると，コンテンツサイズは16085byteらしい．<br><br>
<img width="369" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/174062536-5c168645-caad-431c-8906-6a4918fd5676.png"><br><br>
つまり，サイズ上限を超えないよう何回かに分けてコンテンツを取得し，最終的につなぎ合わせるとよさそうだ．curlコマンドでサイズを指定する際は，-rオプションを使用する．<br><br>
<img width="450" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/174078305-18efd905-478a-414d-a60c-383d94eb05dd.png"><br><br>
`-o ファイル名`でレスポンスの中身を出力できるので，今回は1,2にそれぞれ前半と後半を出力させた．あとは組み合わせてpdfファイルにするだけ．<br>
`cat 1 2 > flag.pdf`<br>
<details>
<summary>galeryの答え</summary>
ctf4b{r4nge_reque5t_1s_u5efu1!}<br><br>
<img width="371" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/174078975-78361182-e0b2-4778-8a48-6a4cf1e92f2c.png">

</details>