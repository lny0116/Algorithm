//내가, 강의에서는 나처럼 정규식을 했는데+ replace(정규식,'')를 이용해서 더 간단하게 풀었음
function solution(s) {
    let answer = 'YES';
    let re = /[a-zA-Z]/gi;
    let arr = s.match(re).join(''); //foundtimestudyYdutsemitDnuof
    let rever = s.match(re).reverse().join('');

    if (arr.toLowerCase() !== rever.toLowerCase()) answer = 'NO'

    console.log(arr);

    return answer;
}

let str = "found7, time: study; Yduts; emit, 7Dnuof";//YES
let str1 = "found7, time: study; Yduts; emit, 8Enuof";//NO
console.log(solution(str));
console.log(solution(str1));