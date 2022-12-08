// //내가 - sort를 이용해서 정렬해서 앞에 것 빼옴
// function solution(arr) {
//     let answer;

//     arr.sort((a, b) => a - b);
//     // console.log(arr)

//     return answer = arr.shift();
// }

// let arr = [5, 7, 1, 3, 2, 9, 11]; //1
// // let arr = [5, 3, 7, 11, 2, 15, 17]; //2
// console.log(solution(arr));

// //강의 - sort 성능적으로 느림 [근데, 코테 수준에선 상관 없음]
// function solution(arr) {
//     let answer, min = arr[0];

//     for (i = 1; i < arr.length; i++) {
//         if (arr[i] < min) min = arr[i];
//     }
//     return answer = min;
// }

// // let arr = [5, 7, 1, 3, 2, 9, 11]; //1
// let arr = [5, 3, 7, 11, 2, 15, 17]; //2
// console.log(solution(arr));

//보충 강의-> 가장 쉬운 풀이 spread 연산자 사용
function solution(arr) {
    let answer = Math.min(...arr); // spread 사용시 -> (arr[0],arr[1],arr[2],...) 이렇게 펼쳐지는 거
    return answer;
}

let arr = [5, 7, 1, 3, 2, 9, 11]; //1
// let arr = [5, 3, 7, 11, 2, 15, 17]; //2
console.log(solution(arr));