function solution(s) {
    var answer = [];

    let st = s.split(' ');

    for (let i of st) {
        answer.push(i.substr(0, 1).toUpperCase() + i.substr(1, i.length).toLowerCase())
    }

    return answer.join(' ');
}
