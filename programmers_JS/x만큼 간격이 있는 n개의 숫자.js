function solution(x, n) {
    var answer = [];

    for (let i = 1; i <= n; i++) {
        answer.push(x * i) //x의 배수
    }

    return answer;
}