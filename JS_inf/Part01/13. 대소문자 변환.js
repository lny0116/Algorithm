//내가
function solution(s) {
    let answer = "";

    for (let v of s) {
        if (v === v.toUpperCase()) answer+=v.toLowerCase();
        else answer+=v.toUpperCase();
    }

    return answer;
}

console.log(solution("StuDY"));//sTUdy