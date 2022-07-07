# Q1. CCTV
<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/177669010-bf4e68ac-10b8-4768-96a6-51e0db82f8b1.png"><br><br>

1問目はログイン認証問題．まずはソースを見に行こう．するとhtml内にパスワード確認っぽい処理をしている部分が見つかる．

~~~
const checkPassword = () => {
  const v = document.getElementById("password").value;
  const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));

  if(p[0] === 52037 &&
     p[6] === 52081 &&
     p[5] === 52063 &&
     p[1] === 52077 &&
     p[9] === 52077 &&
     p[10] === 52080 &&
     p[4] === 52046 &&
     p[3] === 52066 &&
     p[8] === 52085 &&
     p[7] === 52081 &&
     p[2] === 52077 &&
     p[11] === 52066) {
    window.location.replace(v + ".html");
  } else {
    alert("Wrong password!");
  }
}
~~~

使用されている関数の意味を調べながら確認していくと，どうやらパスワードの文字列のi番目をアスキーコード変換し，0xcafeを加えた結果がp\[i\]になるようだ．たとえば，パスワードの0文字目のアスキーコードをXとすると，

~~~
X + 0xcafe = 52037
      ↓
X + 51966 = 52037
      ↓
X = 71
~~~
このように簡単にXを求めることができる．なお，71というアスキーコードを文字に変換すると'G'となる．残りの11文字についても同様の方法で求め，パスワードが"GoodPassword"であることが分かった．ログインすると左下にflagがあった．<br><br>

<details>
<summary>Q1.CCTVの答え</summary>
CTF{IJustHopeThisIsNotOnShodan}<br><br>
<img width="960" alt="キャプチャ" src="https://user-images.githubusercontent.com/64766627/177671765-cd240b76-af02-4203-9ca6-19b747ab0458.png">
</details>