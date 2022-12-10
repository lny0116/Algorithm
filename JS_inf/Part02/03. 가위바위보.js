//내가 풀긴 했는데, 떠올리는 시간이 길어서 다시 풀어보는 게 좋을듯
function solution(a, b) {
    let answer = "";

    for (i = 0; i < a.length; i++) { //&&연산자를 쓴 게 아니고 >,< 이딴거 써서 헤맴ㅋㅋ
        if ((a[i] === 1 && b[i] === 2) || (a[i] === 2 && b[i] === 3) || (a[i] === 3 && b[i] === 1)) answer += 'B'
        else if ((a[i] === 1 && b[i] === 3) || (a[i] === 2 && b[i] === 1) || (a[i] === 3 && b[i] === 2)) answer += 'A'
        else answer += 'D'
    }

    return answer;
}

// 1:가위, 2:바위, 3:보
let a = [2, 3, 3, 1, 3];
let b = [1, 1, 2, 2, 3];
console.log(solution(a, b));// a,b,a,b,d