function solution(s) {
  // if (isNaN(s)) return false;
  // else return true;

  // if (s.length === 4 || s.length === 6) {
  //     if (isNaN(s)) return false;
  //     else return true;
  // } else return false
  // 테스트케이스 11의 오류내용을 살펴보니 자바스크립트에서 숫제에 e가 붙을 경우 지수 표기법으로 인식하여 문자인 경우에도 숫자로 인식해서 일어나는 오류라서, 이것까지 생각해야한다고 함...

  if (s.length === 4 || s.length === 6) {
    for (i = 0; i < s.length; i++) {
      if (isNaN(s[i])) return false;
    }
    return true;
  } else return false;
}
