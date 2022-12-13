function solution(n, arr) {
    let answer, max = Number.MIN_SAFE_INTEGER;

    for (let v of arr) {
        let sum = String(v).split('').reduce((a, b) => a + Number(b), 0);

        if (sum > max) {
            max = sum;
            answer = v;
        } else if (sum === max) {
            if (v > answer) answer = v;
        }
    }

    return answer;
}

let arr = [128, 460, 603, 40, 521, 137, 123]; //137
let arr1 = [235, 1234]; //1234
console.log(solution(7, arr));
console.log(solution(2, arr1));