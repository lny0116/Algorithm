function solution(absolutes, signs) {
    let add = 0;
    let sub = 0;
    let sum = 0;
    
    for (i=0;i<absolutes.length;i++){
        if ((absolutes[i] && signs[i]) === true) {
            add += absolutes[i]
        } else if ((absolutes[i] && signs[i]) === false) {
            sub -= absolutes[i]
        }
        sum = add + sub;
    }
    return sum;
}
