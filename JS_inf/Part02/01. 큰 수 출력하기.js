//내가
function solution(arr) {
    let answer = [arr[0]];

    for (i = 0; i < arr.length - 1; i++) {
        if (arr[i] < arr[i + 1]) answer.push(arr[i + 1])
    }

    return answer;
}

let arr = [7, 3, 9, 5, 6, 12];
// let arr = [7, 8, 2, 7, 3, 4]; //7,8,7,4
console.log(solution(arr));//7 9 6 12