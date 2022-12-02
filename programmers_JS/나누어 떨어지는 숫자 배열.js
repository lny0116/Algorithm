function solution(arr, divisor) {
    var answer = [];
    let temp = [];
    
    for (i=0;i<arr.length;i++){
        if (arr[i] % divisor === 0) {
            answer.push(arr[i])
        } else temp.push(arr[i])
    }
    
    if (answer.length >= 1) return answer.sort((a,b)=>a-b)
    else return [-1];
}
