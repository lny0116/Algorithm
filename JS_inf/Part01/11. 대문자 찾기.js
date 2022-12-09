// //정규식으로 풀려고 했는데, 생각한 대로 안 되어서 강의 봤음.
// function solution(s) {
//     let answer = 0;

//     for (let v of s) {
//         if (v === v.toUpperCase()) answer += 1;
//     }

//     return answer;
// }

// let str = "KoreaTimeGood";
// console.log(solution(str));//3

//내가 생각한 방법대로 푼 게 있어서 찾아옴
function solution(s) {
    let answer = s.match(/[A-Z]/g).length;
    // console.log(s.match(/[A-Z]/g)); //[ 'K', 'T', 'G' ]

    return answer;
}

let str = "KoreaTimeGood";
console.log(solution(str));//3

// //아스키 코드 방법, 대문자 65~90 , 소문자 97~122
// function solution(s) {
//     let answer = 0;

//     for (let v of s){
//         let num = v.charCodeAt();
//         if (65<=num && num<=90) answer+=1;
//         /*여기서 의문이 범위 65 <= num <=90이 왜 안 되는 거지? 했는데
//         '한꺼번에 범위를 지정해서 하는 연산은 파이썬만 됩니다.' ㅋㅋ*/
//     }

//     return answer;
// }

// let str = "KoreaTimeGood";
// console.log(solution(str));//3