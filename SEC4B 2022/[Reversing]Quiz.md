# Quiz
渡されたファイルのフォーマットを`file`コマンドで調べると，ELFファイルであることが分かるのでLinux環境で実行．すると以下のようなクイズが表示されるので，答えていく<br><br>
![キャプチャ](https://user-images.githubusercontent.com/64766627/172317005-c8786275-6e49-4efb-8e82-892ae55d427c.png)<br><br>
4問目にflagは何か聞かれるけど，現時点では分からない．ただ，クイズの3問目でstringsコマンドについて触れられているので，ctfでフィルターをかけて試してみる．<br>
`strings quiz | grep ctf`<br>
これであっさりとflagが入手できた．
<details>
<summary>Quizの答え</summary>
ctf4b{w0w_d1d_y0u_ca7ch_7h3_fl4g_1n_0n3_sh07?}
</details>