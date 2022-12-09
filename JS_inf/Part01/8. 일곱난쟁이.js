//제대로 못 풀었어서 강의 보면서 풀었음. 다시 풀어봐야 할 문제임
function solution(arr) {
    let answer = arr;
    let sum = 0;

    for (let v of arr) {
        sum += v; //배열 총 합 구한 거고 - 140
    }

    end:
    for (i = 0; i < arr.length - 1; i++) {
        for (j = 1; j < arr.length; j++) {
            if ((sum - (arr[i] + arr[j])) === 100) {
                // answer.splice(i, 1) //이렇게 i부터 지워버리면 답이 -> 15, 8이 지워져버림
                // answer.splice(j, 1) //이유는 splice로 지움으로써 인덱스가 당겨져서 [6]번째로 된 8이 지워진 것.
                answer.splice(j, 1) //이렇게 마지막 인덱스부터 없애버리면 해결.
                answer.splice(i, 1)
                break end;
            }
        }
    }

    return answer;
}

// let arr = [20, 7, 23, 19, 10, 15, 25, 8, 13];//20 7 23 19 10 8 13
let arr = [20, 7, 23, 19, 10, 15, 28, 8, 13];//[7, 19, 10, 15, 28, 8, 13] - 예외 케이스(조건이 맞는 모든 배열을 없애는 걸 방지)
console.log(solution(arr));

// break문은 label을 이용.
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/break