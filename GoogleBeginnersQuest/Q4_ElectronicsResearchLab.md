# Q4. Electronics Research Lab

恐らく正規の解き方じゃなかった気がするが，解けてしまったので解説．2つのファイルが配布されるが，chal.cを見てみる．c言語で書かれているものの見慣れない関数ばかりだったので調べてみると，どうやらラズパイを動かすためのコードであることがわかった．例えば，for文内の冒頭にある以下のコードでは<br><br>

~~~
gpio_set_mask(67);
gpio_clr_mask(0);
~~~
<br>
gpio_set_mask(67)では67，すなわち0100 0011の1にあたるピンをhighにし，gpio_clr_mask(0)では0000 0000の1にあたるピンをlowにすることを表している．ここで67という値は，10進数のアスキーコードとして変換すると'C'を表している．これって"CTF{..."と続くでは！？と思ったのでもう少し検証してみる．<br><br>

~~~
gpio_set_mask(67);	//67
gpio_clr_mask(0);	//-0
sleep_us(100);	//67=>C
gpio_set_mask(20);	//+20
gpio_clr_mask(3);	//-3
sleep_us(100);	//84=>T
gpio_set_mask(2);	//+2
gpio_clr_mask(16);	//-16
sleep_us(100);	//70=>F
gpio_set_mask(57);	//+57
gpio_clr_mask(4);	//-4
sleep_us(100);	//123=>{
~~~
<br>
仮説は正しかったようだ．このまま計算してflagを入手した．<br><br>

<details>
<summary>Q4.Electronics Research Labの答え</summary>
CTF{be65dfa2355e5309808a7720a615bca8c82a13d7}<br><br>


</details>