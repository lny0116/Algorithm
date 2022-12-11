function solution(arr) {
    let answer = 0;

    let dx = [-1, 0, 1, 0], dy = [0, 1, 0, -1];

    for (i = 0; i < arr.length; i++) {
        for (j = 0; j < arr.length; j++) {
            let flag = 1; //일단 맞다고 초기화
            for (k = 0; k < dx.length; k++) { //dx, dy의 length (4방향 보는 거)
                let nx = i + dx[k];
                let ny = j + dy[k];
                //↓크거나 같으면 봉우리가 아님, 이때 -1인덱스는 범위 밖이니까 오류나, 그래서 안 나게끔
                if (nx >= 0 && ny >= 0 && nx < arr.length && ny < arr.length && arr[nx][ny] >= arr[i][j]) {
                    flag = 0;// 걘 봉우리가 아니다~
                    break; //아닌 애는 더이상 돌 필요가 없으니까
                }
            }
            if (flag === 1) answer += 1; //1이라면 봉우리가 맞으니까 카운트해줌
        }
    }

    return answer;
}

let arr = [[5, 3, 7, 2, 3],
[3, 7, 1, 6, 1],
[7, 2, 5, 3, 4],
[4, 3, 6, 4, 1],
[8, 7, 3, 5, 2]]; //10
console.log(solution(arr));