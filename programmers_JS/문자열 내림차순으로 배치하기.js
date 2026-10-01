function solution(s) {
    let answer = '';
    
    // console.log(s)
    
    // for(i=0;i<s.length;i++) {
    //     let arr = [s[i]]
    //     console.log(arr)
    // }
    
    answer = s.split('').sort().reverse().join('');
    //각 문자를 배열로 만든 후, 사전식sort 배열을 하고 reverse를 한 후 Join으로 합침
    
    return answer;
}