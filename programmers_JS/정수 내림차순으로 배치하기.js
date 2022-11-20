function solution(n) {
    var answer = Number(n.toString().split("").sort().reverse().join(""));
    
    return answer;
}
