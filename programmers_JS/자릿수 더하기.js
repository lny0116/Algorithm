function solution(n)
{
    var answer = 0;
    let sliceNum = n.toString().slice(0, n.length);
    let sum = 0;
    
    for (i = 0; i < sliceNum.length; i++){
        sum += Number(sliceNum[i])
    }

    return answer = sum;
}
