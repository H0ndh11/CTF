#include <stdio.h>

int main(void){
    long long int x=0,i;
    for(i=0;;i++){
        x = i * 1584891 + 32134;
        //printf("%lld\n",x);   //確認用
        if(x % 3438478 == 193127){
            printf("%lld\n",x);
            printf("result %% 1584891: %lld\n", x%1584891);
            printf("result %% 3438478: %lld\n", x%3438478);
            break;
        }
    }
}