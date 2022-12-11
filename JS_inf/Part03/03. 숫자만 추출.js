//내가, 그 앞에 자연수로 변환했을 때 0은 어차피 지워진다고 하길래 약간 수정함
function solution(str) {
    let answer;

    let re = /[0-9]/g;
    let arr = str.match(re);

    // if (arr[0] === '0') arr.shift();

    answer = arr.join('');

    // console.log(answer)
    // console.log(typeof(Number(answer)))

    return Number(answer);
}

let str = "g0en2T0s8eSoft"; //208
let str1 = 'tge0a1h205er'; //1205
console.log(solution(str));
console.log(solution(str1));

//강의에서는 inNaN()을 사용함
//https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN