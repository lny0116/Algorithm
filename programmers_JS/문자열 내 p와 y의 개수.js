function solution(s){
    var answer = true;
    
    // if문이 본인이 푼 건데, 이게 2, 3번째에서 런타임 에러가 계속 발생. 알아봤더니, p와 y가 둘 다 없는 경우가 문제 -> 옵셔널 체이닝(?.)을 이용하면 통과함.
    if ((s.match(/p/gi) === null && s.match(/y/gi) === null) || (s.match(/p/gi)?.length === s.match(/y/gi)?.length)) return answer;
    else return !answer;
    
    // return s.toLowerCase().split('p').length === s.toLowerCase().split('y').length
    
    // return s.match(/p/ig)?.length == s.match(/y/ig)?.length;
}
