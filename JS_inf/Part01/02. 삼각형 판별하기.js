//문제 이해가 어려워서 설명을 들음 '긴 막대< 짧은 막대 2개의 합 이어야 yes인 것'
//내가 푼 거
function solution(a, b, c) {
    let sum = a + b + c;
    let max = Math.max(a, b, c);

    if ((sum - max) > max) return 'YES';
    else return 'NO';
}

console.log(solution(13, 33, 17)); //no
console.log(solution(6, 7, 11)); //yes
console.log(solution(7, 5, 2)); //no