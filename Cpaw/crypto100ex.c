#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char* argv[]){
  int i;
  int j;
  int key;
  //int key = atoi(argv[2]);	//引数2（数字）を文字列から数値への変換
  const char* flag = argv[1];	//flagに引数1（暗号文）を代入
  /*つまり
  crypto100.exe 暗号文 鍵
  で解読するイメージ
  */
  for(key=1;key<=32;key++){
    printf("cpaw{");
    /*
    i=key-1 から i=暗号文の長さ(31) までiを増やしながらループ
      j=i から j=i-key+1 までjを減らしながらループ
        j番目のflag文字列を出力
    */
    for(i = key - 1; i <= strlen(flag); i+=key) for(j = i; j>= i - key + 1; j--) printf("%c", flag[j]);
    printf("}\n");
  }
  return 0;
}
