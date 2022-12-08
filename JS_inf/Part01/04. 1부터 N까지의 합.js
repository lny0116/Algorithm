//내가
function solution(n) {
    let answer = 0;

    for (i = 1; i <= n; i++) {
        answer += i;
    }

    return answer;
}

console.log(solution(10)); //55
console.log(solution(6)); //21