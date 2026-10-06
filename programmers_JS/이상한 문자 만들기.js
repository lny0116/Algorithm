function solution(s) {
  const arr = s.split(" ");
  // console.log(arr)
  let result = []; // 단어들을 담을 배열

  for (let i = 0; i < arr.length; i++) {
    const now = arr[i];
    // console.log(now)
    let word = ""; // 변환된 하나의 단어를 담을 변수

    for (let j = 0; j < now.length; j++) {
      if (j % 2 === 0) {
        word += now[j].toUpperCase();
      } else {
        word += now[j].toLowerCase();
      }
    }

    result.push(word);
  }

  return result.join(" ");
}