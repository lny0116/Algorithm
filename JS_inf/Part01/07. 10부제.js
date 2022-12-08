//일의 자리를 어떻게 해야할지 모르겠어서 강의 봤음. 다시 풀어봐야함!!
function solution(day, arr) {
    let answer = 0;

    for (let v of arr) {
        if (v % 10 === day) answer += 1;
    }

    return answer;
}

arr = [25, 23, 11, 47, 53, 17, 33];//3
arr2 = [12, 20, 54, 30, 87, 91, 30];//3
arr3 = [02, 22, 54, 32, 82, 91, 30];//4
console.log(solution(3, arr));
console.log(solution(0, arr2));
console.log(solution(2, arr3));