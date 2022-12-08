//내가 먼저 푼 것
function solution(a, b, c) {
    let answer = Math.min(a, b, c);

    return answer;
}

console.log(solution(2, 5, 1)); //1
console.log(solution(6, 5, 11)); //5
console.log(solution(6, 5, 2)); //5

//강의가 푼 것
function solution(a, b, c) {
    let answer;

    if (a > b) answer = b;
    else answer = a;

    if (answer > c) answer = c;

    return answer;
}

console.log(solution(2, 5, 1)); //1
console.log(solution(6, 5, 11)); //5