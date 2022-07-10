function controlCar(scanArray){
    
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

}