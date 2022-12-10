//내가, 근데 틀린 거 같아서 다시 수정했는데, 값을 갱신을 못 시켜서 강의봄;
function solution(arr) {
    let answer = 1; //130 애는 무조건 보일 테니까

    let min = arr[0]; //기준값 130 그리고 그 이상이어야됨

    for (i = 1; i < arr.length; i++) {
        if (min < arr[i]) {
            answer += 1;
            min = arr[i] //이걸 못했음 ㅋㅋ
        }
    }

    return answer;
}

// let arr = [130, 135, 148, 140, 145, 150, 150, 153];//5
let arr = [130, 129, 130, 131, 145, 150, 152, 153];//6
console.log(solution(arr));