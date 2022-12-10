//강의 봄
function solution(arr) {
    let answer;
    let row = column = diaLeft = diaRight = 0;

    for (i = 0; i < arr.length; i++) {
        row = column = 0; //초기화 해줌
        for (j = 0; j < arr.length; j++) {
            row += arr[i][j]; // arr[0][0~4]도는 거임 == 행
            column += arr[j][i]; // arr[0~4][0]도는 거임 == 열
        }
        diaLeft += arr[i][i]; //왼쪽부터 대각선
        diaRight += arr[i][arr.length-1-i] //오른쪽부터 대각선
    }

    return answer = Math.max(row, column, diaLeft, diaRight);
}

let arr = [[10, 13, 10, 12, 15],
[12, 39, 30, 23, 11],
[11, 25, 50, 53, 15],
[19, 27, 29, 37, 27],
[19, 13, 30, 13, 19]]; //155
console.log(solution(arr));