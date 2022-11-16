function solution(n) {
    var answer = [];
    let arr = n.toString().slice(0, n.length);
    
    for (i = 0; i< arr.length; i++){
        answer.push(parseInt(arr[i]))
    }
    
    answer.reverse();
    
    return answer;
}
