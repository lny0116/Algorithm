//내가
function solution(s, t) {
    let answer = 0;

    for (let v of s) {
        if (v === t) answer += 1;
    }

    return answer;
}

let str = "COMPUTERPROGRAMMING";
console.log(solution(str, 'R')); //3
console.log(solution(str, 'G')); //2