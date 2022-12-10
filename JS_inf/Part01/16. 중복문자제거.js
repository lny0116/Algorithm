// //내가, 중복 제거 어떻게 하는 지 몰라서 검색해서 풀었는데 이건 배열로 나오고..
// function solution(s) {
//     let answer = "";

//     let set = new Set(s);
//     // console.log(set)


//     return answer = [...set];
// }
// console.log(solution("ksekkset"));//kset

//강의 본 것 indexOf()는 특정값이 처음으로 나타나는 index를 리턴함
function solution(s) {
    let answer = '';

    for (i = 0; i < s.length; i++) {
        // console.log(s.indexOf(s[i]));
        if (i === s.indexOf(s[i])) answer += s[i];
        //자신의 index와 일치하는 것만 출력시킴
    }

    return answer;
}
console.log(solution("ksekkset"));//kset