// function solution(n)
// {
//     var answer = 0;
//     let sliceNum = n.toString().slice(0, n.length);
//     let sum = 0;
    
//     for (i = 0; i < sliceNum.length; i++){
//         sum += Number(sliceNum[i])
//     }

//     return answer = sum;
// }

// 서잘데기 없는 것 수정... ㅎㅎ

function solution(n)
{
    var answer = 0;
    let str = String(n);
       
    for (i = 0; i < str.length; i++){
        answer += Number(str[i])
    }

    return answer;
}
