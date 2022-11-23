// function solution(a, b) {
//     var answer = 0;
//     let sum = [];
    
//     if (a<=b){
//         for (i=a; i<=b; i++){
//             sum.push(i);
//             answer = sum.reduce((acc, cur)=>acc+cur,0);
//         }
//     } else {
//         for (i=b; i<=a; i++){
//             sum.push(i);
//             answer = sum.reduce((acc, cur)=>acc+cur,0);
//         }        
//     }
    
//     return answer;
// }

// 처음 생각했던 방식은 시간이 초과됨ㅠㅠ 그래서 다른 방법을 알아본 게 아래

function solution(a, b) {
  let answer = 0;
  for (i = Math.min(a, b); i <= Math.max(a, b); i++) {
    answer += i;
  }
  return answer;
}
