// 강의 참고
function solution(arr) {
    let answer = Array.from({ length: arr.length }, () => 1); //[ 1, 1, 1, 1, 1 ]

    for (i = 0; i < arr.length; i++) {
        for (j = 0; j < arr.length; j++) {
            if (arr[i] < arr[j]) answer[i]++;
        }
    }

    return answer;
}

// let arr = [87, 89, 92, 100, 76]; // 4 3 2 1 5
let arr = [92, 92, 92, 100, 76]; // [ 2, 2, 2, 1, 5 ]
console.log(solution(arr));

// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from