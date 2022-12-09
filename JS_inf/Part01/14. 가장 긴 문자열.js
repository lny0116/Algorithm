//내가
function solution(s) {
    let answer = '';
    let temp = [];
    let num;

    for (let v of s) {
        temp.push(v.length)
    }

    temp.sort((a, b) => a - b)
    num = temp.pop()

    for (let v of s) {
        if (num === v.length) answer += v
    }

    return answer;
}

let str = ["teacher", "time", "student", "beautiful", "good"];
console.log(solution(str));//beautiful