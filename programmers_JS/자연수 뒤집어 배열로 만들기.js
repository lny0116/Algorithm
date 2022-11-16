// function solution(n) {
//     var answer = [];
//     let arr = n.toString().slice(0, n.length);
    
//     for (i = 0; i< arr.length; i++){
//         answer.push(parseInt(arr[i]))
//     }
    
//     answer.reverse();
    
//     return answer;
// }

// let arr = n.toString().slice(0, n.length); -> 이 부분이 서잘데기가 없음...ㅎ

function solution(n) {
    var answer = [];
    let arr = String(n);
    
    for (i = 0; i< arr.length; i++){
        answer.push(parseInt(arr[i]))
    }
    
    answer.reverse();
    
    return answer;
}
