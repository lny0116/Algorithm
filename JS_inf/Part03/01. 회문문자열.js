//내가 풀긴 했는데, 시간이 많이 걸렸으니까 다시 풀어보자 ㅎㅎ
//강의에서는 split().reverse().join() 이용해서 풀었음 ㅋㅋ 더 간단하게
function solution(s) {
    let answer = 'yes';

    let sp = s.toUpperCase().split(''); //[ 'g', 'o', 'o', 'G' ]
    let re = [...sp].reverse(); //[ 'G', 'o', 'o', 'g' ]

    // console.log(sp);
    // console.log(re);

    for (i = 0; i < s.length; i++) {
        if (sp[i] !== re[i]) answer = 'no';
    }

    return answer;
}

let str = "gooG"; //yes
let str1 = "gooD"; //no
let str2 = "Ioi"; //yes
console.log(solution(str));
console.log(solution(str1));
console.log(solution(str2));

// //강의
// function solution(s) {
//     let answer = 'YES';

//     s = s.toUpperCase();
//     let len = s.length; //4

//     for (i = 0; i < Math.floor(len / 2); i++) {
//         if (s[i] !== s[len - 1 - i]) answer = 'NO' //index는 -1이니까
//     }

//     return answer;
// }

// let str = "gooG"; //yes
// let str1 = "gooD"; //no
// let str2 = "Ioi"; //yes
// console.log(solution(str));
// console.log(solution(str1));
// console.log(solution(str2));