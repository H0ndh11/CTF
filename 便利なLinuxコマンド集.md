# Linuxコマンド

CTFでよく使うコマンドを書いておく場所．コマンドとオプションは随時追加されていく
- [Linuxコマンド](#linuxコマンド)
  - [file](#file)
  - [string](#string)
  - [netcat nc](#netcat-nc)
  - [curl](#curl)
  - [binwalk](#binwalk)
  - [gobuster, ffuf, dirb](#gobuster-ffuf-dirb)

## file
`file [ファイル名]`<br>
得体のしれないファイルを渡されたときはまずこれを試す．ファイルのフォーマットがわかる．

## string
`string [ファイル名]`<br>
ファイル内から文字列を抽出・表示するコマンド．一見関係なさそうなpngファイルとかもテキストが格納できる部分に書かれていることがある．grepと併用して<br>
`string [ファイル名] | grep [キーワード]`<br>
と入力すればキーワードを含む文字列だけ抜き出すことが可能．

## netcat nc
`nc [urlまたはipアドレス] [ポート番号]`<br>
問題サーバに接続するコマンド．大抵は接続したらこちらから入力できることが多いので，<br>
`nc [urlまたはipアドレス] [ポート番号] | python -c 'print("hello")'`<br>
のように書くことで接続後の入力も同時に行うことができる．これを応用し，<br>
`nc [urlまたはipアドレス] [ポート番号] | python -c 'print('A'*100)'`<br>
と書くとAを100文字分入力することができる．手入力で100文字打たなくていいのは便利

## curl
`curl [URL]`<br>
URL先のファイルを取得して表示したりダウンロードしたりできる．sqlインジェクションによく使うのかな．あんまりよくわかってないから言語化できたら更新します．オプションは[ここ](https://qiita.com/ryuichi1208/items/e4e1b27ff7d54a66dcd9)がわかりやすい．

## binwalk
ファイルの中に隠れているファイルを見つけることができる．主にフォレンジックの問題で使われる．探すときは<br>
`binwalk [file]`<br>
抽出したいときは<br>
`binwalk -D='.*' [file]`<br>

## gobuster, ffuf, dirb
Webアプリケーションのコンテンツをワードリストから総当たりで探してくれるツール．問題によっては使用禁止．<br>
`gobuster -u [URL] -w [wordlistのパス]`<br>
`ffuf -w [wordlistのパス] -u [URL]/FUZZ`
`dirb [URL] [wordlistのパス]`
wordlistは大抵/usr/share/wordlists内にある．kalilinuxなら標準で付属しているはず．