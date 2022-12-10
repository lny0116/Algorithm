//강의 봄,, 내가 푼 방법도 근접했는데, 답은 아니었음..ㅠㅠ
function solution(arr) {
    let answer = 0;
    let cnt = 0;

    for (let v of arr) {
        if (v === 1) {
            cnt += 1;
            answer += cnt;
        }
        else cnt = 0;
    }

    return answer;
}

// 답이 맞은 문제의 경우에는 1로 표시하고, 틀린 경우에는 0으로 표시
// 1+1+2+3+1+2=10
let arr = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]; //10
// 1+2+1+1+2+3+4=14
// let arr = [1, 1, 0, 0, 1, 0, 1, 1, 1, 1]; //14
console.log(solution(arr));