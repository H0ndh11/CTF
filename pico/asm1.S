asm1:													#入力は0x8be
	<+0>:	push   ebp									#ベースポインタをプッシュ
	<+1>:	mov    ebp,esp								#ベースポインタをスタックポインタにする
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x71c			#ベースポインタ+0x8に格納されている値（4バイト)と0x71cを比較
	<+10>:	jg     0x512 <asm1+37>						#0x71cより大きい場合ジャンプ
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x6cf			
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0x3
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0x3
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x8be			#0x8beと比較
	<+44>:	jne    0x523 <asm1+54>						#等しいのでジャンプしない
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]				#eaxに格納
	<+49>:	sub    eax,0x3								#eaxから0x3を引いて再格納
	<+52>:	jmp    0x529 <asm1+60>						#jmpして終了
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0x3
	<+60>:	pop    ebp
	<+61>:	ret    

