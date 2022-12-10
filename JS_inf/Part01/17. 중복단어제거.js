//내가
function solution(s) {
    let answer = '';

    for (i = 0; i < s.length; i++) {
        // console.log(s.indexOf(s[i]))
        if (i === s.indexOf(s[i])) answer += s[i] + ' ';
    }

    return answer;
}

let str = ["good", "time", "good", "time", "student"];
console.log(solution(str));//good, time, student

// //강의
// function solution(s) {
//     let answer = s.filter((v, i) => { return s.indexOf(v) === i });

//     return answer;
// }

// let str = ["good", "time", "good", "time", "student"];
// console.log(solution(str));//good, time, student