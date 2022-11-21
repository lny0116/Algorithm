function solution(numbers) {
//     let total = 1+2+3+4+5+6+7+8+9;
//     let sum = 0;
    
//     return total - numbers.reduce((acc,cur) => acc+cur, 0);

// 제출은 위 풀이로 했음. 근데 이렇게 풀면 전체 합이 커졌을 때가 문제라고 생각해서 다시 푼 게 아래
    
    let total = 0;
    
    for(i=1; i<=9; i++){
        total += i;
    }
    
    return total - numbers.reduce((acc,cur) => acc+cur, 0);
}
