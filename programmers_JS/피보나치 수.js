function fibo(n) {
    let num = [0, 1, 1];
    for(let i = 3; i <= n; i++) {
      num[i] = (num[i - 1] + num[i - 2])%1234567; 
    }
    return num[n];
}

function solution(n) {
    const answer = fibo(n) % 1234567;
    return answer;
}
