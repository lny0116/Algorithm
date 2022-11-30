function solution(arr) {
    let minNum = Math.min.apply(null, arr); //1
    
    for (i=0;i<arr.length;i++){
        if (arr[i] === 10) {
            return [-1]
        } else if (arr[i] === minNum){
            arr.splice(i, 1);
            i--;
            return arr;
        }
    }
}

//위는 틀림, 75점짜리 정답...

function solution(arr) {
    let minNum = Math.min.apply(null, arr); //1
    
    for (i=0;i<arr.length;i++){
        if (arr[i] === 10) {
            return [-1]
        } else if (arr[i] === minNum){
            arr.splice(i, arr.indexOf(minNum, 1));
            return arr;
        }
    }
}

//위는 최소값에 중복이 있을 때([1,1,2,3]과 같은) 틀리나 싶어서 다음과 같이 짰더니, 테케는 다 맞았으나 이상하게 점수는 더 낮았음..

function solution(arr) {
    arr.splice(arr.indexOf(Math.min(...arr)),1);
  
    if(arr.length<1)return[-1];
    return arr;
}

// 중복은 일어날 수 없는 문제였고... 효율성이 떨어지면 틀린다고 해서.. 다시 풀어봐야 할 
