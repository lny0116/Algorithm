function solution(s) {
  // console.log(s)
  const result = [];
  for (i = 0; i < s.length; i++) {
    // console.log(s[i])
    let found = false;
    for (j = i - 1; j >= 0; j--) {
      // console.log(s[j])
      if (s[i] === s[j]) {
        result.push(i - j);
        found = true;
        break;
      }
    }
    if (found === false) result.push(-1);
  }
  return result;
}

// map 이용해서 풀기 - 다른 사람
function solution(s) {
    const result = [];
    const lastSeen = new Map(); // [글자 : 마지막으로 발견된 인덱스]를 저장할 장부
    console.log(lastSeen)
    
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        console.log(char)
        
        // 장부에 이 글자가 적혀있나요?
        if (lastSeen.has(char)) {
            // 있으면: 현재 위치 - 장부에 적힌 마지막 위치
            result.push(i - lastSeen.get(char));
        } else {
            // 없으면: 처음 본 글자이므로 -1
            result.push(-1);
        }
        
        // 장부에 이 글자의 최신 위치를 현재 인덱스(i)로 업데이트/등록합니다.
        lastSeen.set(char, i);
    }
    
    return result;
}
