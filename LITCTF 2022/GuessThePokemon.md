# Guess The Pokemon
解けなかった問題シリーズその３<br>
ログイン認証問題のように，入力欄と決定ボタンのみが置かれており，正しいポケモンの名前を入力できるとflagがもらえるみたいだ．配布されたmain.py内の

~~~
...

name = request.form['name']

if ("'" in name or "\\" in name or '"' in name):
    return render_template('login.html', error="no quotes or backslashes:)")
elif (name == "names"):
    return render_template('login.html', error="you are wrong :<")
    
try:
    cur.execute("SELECT * FROM pokemon WHERE names=" + name + "")
except:
    render_template('login.html', error="you are wrong :3")

...
~~~
<br>
に注目する．テーブルから入力と一致するpokemonがいるとそれを表示してくれるsql文がある．sqlインジェクションらしいが，`'`と`\\`と`"`は弾かれるようになっていた．また，`names`を入力しても弾かれる．これらを避けてsqlインジェクションを行う方法はいくつかあるみたいだが，今回はスペースを加えて`names `とすることでflagが手に入った．それにしても目に優しくないwebページだった．
<br><br>

<details>
<summary>答え</summary>
LITCTF{flagr3l4t3dt0pok3m0n0rsom3th1ng1dk}
</details>