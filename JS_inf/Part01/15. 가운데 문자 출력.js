// //내가, 근데 주어진 테케는 맞았는데 내가 만든 테케가 안 맞아서 의문임;;
// function solution(s) {
//     let answer;
//     let num = Math.ceil(s.length / 2);
//     //강의 봤더니 이때는 Math.floor 쓰는게 더 나았다.. 내림으로 해주는 거

//     if (num % 2 === 0) { //even
//         answer = s[num - 1] + s[num]
//     } else { //odd
//         answer = s[num - 1]
//     }

//     return answer;
// }

// console.log(solution("study"));//u
// console.log(solution("good"));//oo
// console.log(solution("length"));//ng
// console.log(solution("hello"));//l
// console.log(solution("abcdef"));//cd

//내가 다시 푼 거, 강의에서는 substring ,substr 썼음.
function solution(s) {
    let answer;
    let num = Math.floor(s.length / 2);

    if (s.length % 2 !== 0) { //odd
        answer = s[num]
    } else { //even
        answer = s[num - 1] + s[num]
    }

    return answer;
}

console.log(solution("study"));//u
console.log(solution("good"));//oo
console.log(solution("length"));//ng
console.log(solution("hello"));//l
console.log(solution("abcdef"));//cd

/*
substring(start index, end index)
-> substring(1,2)하면 1번 인덱스만 뽑힘
substr(start index, start index to next index) -> study(0,1,2,3,4) -> t뽑
-> substr(1,2)하면 1번 인덱스부터 2개 뽑음 -> good(0,1,2,3) -> oo뽑
*/