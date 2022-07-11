<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/178144112-1334c2dd-42d2-4a65-9aea-17fd911a0170.png"><br><br>

自動運転プログラムを作る問題．画像左上が自分の車で，前にいる車をぶつからずに追い抜く．右の説明にもあるように，scanArrayには以下の画像のような距離を示す値が配列として格納されている．なお，scanArray\[8\]は常に自身の車の中心を表すため，自身が移動すればscanArrayの各値が示す距離の位置も変わる．<br><br>

<img width="960" alt="キャプチャ2" src="https://user-images.githubusercontent.com/64766627/178144141-05828a05-e814-4554-b911-886ddd63252e.PNG"><br><br>
controlCar(scanArray)の返り値には-1,0,1のいずれかであり，それぞれ左に1移動，直進，右に1移動となっている．ここでの1移動というのは，scanArrayでも用いられたように，1車線移動ではなく1/4車線移動するという点に注意．<br><br>

ここからプログラムの組み方を解説をしていくが，スクリプトのみ確認したい場合はこちらの[drive.js](https://github.com/H0ndh11/CTF/blob/main/GoogleBeginnersQuest/drive.js)へ．<br><br>

以上を踏まえると，スクリプトは2つのステップに分けて書いていくのがよさそう．step1ではscanArrayから通れそうな道を探す．step2では通れそうな道に向かってハンドルを操作する．step1はこのように書いた．<br><br>

~~~
//step1:2つ以上の連続するindexで共に最も大きい値をとるものを探す(iはその中で最も小さい値)
//これで線以外で安全な車線がどこにあるのかがわかる
let max_index=7;
let max_value=0;
for(let i=0;i<17;i++){
    if(max_value<scanArray[i]&&scanArray[i]==scanArray[i+1]){
        max_value=scanArray[i];
        max_index=i;
    }
}
~~~
<br>
scanArray配列には，0~16の計17個の値が距離として格納されている．これらの値を比較し，最も距離がある2つ以上連続したインデックスを探す．なぜ連続したインデックスなのかというと，最も距離がある値のみを探すと必然的に車と車の間に位置するセンターラインが選ばれてしまう．そのため連続したインデックスを用いている．これにより，例えば上の補足画像における状況ではmax_indexに3が入ることとなる．続いてstep2．<br><br>

~~~
//step2:安全な車線へ向けて移動
if(max_index<7){
    return -1;
}
else if(max_index>7){
    return 1;
}
else{
    return 0;
}
~~~
<br>
これは解説するまでもないが，step1で安全な車線が分かったので7を基準にしてmax_indexの値によってハンドルをきる方向を判断している．