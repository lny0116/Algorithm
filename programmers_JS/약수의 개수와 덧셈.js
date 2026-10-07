function solution(left, right) {
    let result = 0;

    for (i = left; i <= right; i++) {
        // console.log(i)

        if (Math.sqrt(i) % 1 === 0) { // 제곱근 이용 + 나머지 연산자 이용
            result -= i
        } else {
            result += i
        }
    }
    return result
}