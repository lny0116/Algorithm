function solution(x) {
  let sum = 0;
  
  let arr = String(x).split("");
  // 입력받는 정수 x를 문자열로 형변환 해준 후, 한글자씩 나누고 arr라는 배열에 대입

  for (let i = 0; i < arr.length; i++) {
    sum += Number(arr[i]);
  }
  //arr의 인덱스 하나씩 올려주면서 각 원소들을 sum에 더함

  return x % sum == 0 ? true : false;
  // x를 sum으로 나눈 나머지가 0 이면 true, false 가 반환되는 삼항연산자로 마무리
}
