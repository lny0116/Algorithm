function solution(seoul) {
    let where = [];
    
    for (i=0;i<seoul.length;i++){
        if (seoul[i] === 'Kim'){
            where.push(i);
            // console.log(where);
        }
    }
    
    return answer = `김서방은 ${where[0]}에 있다`;
}
