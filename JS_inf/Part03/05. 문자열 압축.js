//거의 근접했는데... 그 문자열에 숫자를 어떻게 추가할 지 감이 안 와서 강의봄ㅠ
function solution(s) {
    let answer = '';
    let cnt = 1;

    for (i = 0; i < s.length; i++) {
        if (s[i] === s[i + 1]) {
            cnt++;
        } else {
            answer += s[i];
            if (cnt > 1) answer += String(cnt);
            cnt = 1;
        }
    }

    return answer;
}

let str = "KKHSSSSSSSE"; //K2HS7E
console.log(solution(str));