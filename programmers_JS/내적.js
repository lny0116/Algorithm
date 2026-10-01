function solution(a, b) {
  let sum = 0;

  for (i = 0; i < a.length; i++) { // a,b가 길이가 같음
    // console.log(a[i])
    sum += a[i] * b[i];
  }
  return sum;
}
