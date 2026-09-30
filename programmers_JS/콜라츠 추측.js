function solution(num) {
    let result = num;
    let i = 0; //i를 변수로도 for문 안에서 활용하려면 for 문 밖에서 미리 선언하고
    for(;i <= 500; i++){ //for 문 조건 안에는 ;이 2번 들어가야 한다함
        if (result === 1) {
            return i;
        } else if (result % 2 !== 0) {
            result = (result * 3) + 1;
        } else if (result % 2 === 0) {
            result = result / 2;
        } 
    }
    return -1; // for 문에 500번 제한을 걸었으므로 for 문이 성과없이 끝났다면 -1을 리턴
}