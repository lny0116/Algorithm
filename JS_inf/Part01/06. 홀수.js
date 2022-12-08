//내가
function solution(arr) {
    let answer = [], odd = [];
    let sum = 0;

    for (i = 0; i < arr.length; i++) {
        if (arr[i] % 2 !== 0) {
            sum += arr[i]
            odd.push(arr[i])
        }
    }

    let min = Math.min(...odd);

    answer.push(sum, min)

    return answer;
}

arr = [12, 77, 38, 41, 53, 92, 85]; //256, 41
console.log(solution(arr));

//강의 - for of 문
function solution(arr) {
    let answer = [], odd = [];
    let sum = 0;

    for (let v of arr) {
        if (v % 2 !== 0) {
            sum += v
            odd.push(v)
        }
    }

    let min = Math.min(...odd);

    answer.push(sum, min)

    return answer;
}

arr = [12, 77, 38, 41, 53, 92, 85]; //256, 41
console.log(solution(arr));