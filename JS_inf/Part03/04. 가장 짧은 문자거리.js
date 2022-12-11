//강의
function solution(s, t) {
    let answer = [];

    let max = 1000; //문자열의 길이는 100을 넘지 않는다.

    for (let v of s) {
        if (v === t) {
            max = 0;
            answer.push(max);
        } else {
            max++;
            answer.push(max);
        }
    }

    max = 1000; //앞에서 했던 숫자 다시 초기화 해주는 것

    for (i = s.length - 1; i >= 0; i--) {
        if (s[i] === t) {
            max = 0; // 어차피 0인 곳이니까, 초기화만 해줌
        } else {
            max++;
            answer[i] = Math.min(answer[i], max);
        }
    }

    return answer;
}

let str = "teachermode"; //1 0 1 2 1 0 1 2 2 1 0
console.log(solution(str, 'e'));