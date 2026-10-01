function solution(t, p) {
  let cnt = 0;

  for (i = 0; i <= t.length - p.length; i++) { //등호(=)를 붙이지 않으면 마지막 부분 문자열을 검사하지 못하고 건너뜀;;
    let num = t.substr(i, p.length); // substr()은 String 인스턴스에서 전달받은 시작 인덱스부터 길이만큼의 문자열을 추출한 새로운 문자열을 반환함.
    // console.log(typeof(num))
    if (Number(num) <= Number(p)) cnt++;
  }
  return cnt;
}
