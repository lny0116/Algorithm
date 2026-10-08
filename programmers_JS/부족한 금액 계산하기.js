function solution(price, money, count) {
    let total = 0;

    for (let i = 1; i <= count; i++) {
        // console.log(i)
        total += price * i
    }

    // console.log(total)

    const answer = total > money ? total - money : 0;


    return answer;
}