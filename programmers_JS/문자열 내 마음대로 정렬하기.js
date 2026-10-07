function solution(strings, n) {
    const arr = [];

    for (let i = 0; i < strings.length; i++) {
        let word = strings[i];
        arr.push({ char: word[n], word: word }); // { 기준글자, 전체단어 }
    }

    arr.sort((a, b) => {
        // n번째 글자가 다르면 글자 기준으로 사전순 정렬
        if (a.char !== b.char) {
            return a.char.localeCompare(b.char);
        }
        // n번째 글자가 같으면 전체 단어 기준으로 사전순 정렬
        return a.word.localeCompare(b.word);
    });

    // 정렬된 arr에서 원래 단어(word)만 뽑아서 새 배열로
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(arr[i].word);
    }

    return result;
}

// 남이 한 코드 - 내 방식에서 좀 더 간단하게
function solution(strings, n) {
    // strings 배열을 내부 조건에 따라 정렬합니다.
    strings.sort((a, b) => {
        // 1. 먼저 n번째 글자를 서로 비교합니다.
        if (a[n] > b[n]) return 1;   // a[n]이 뒤에 와야 하면 양수 반환
        if (a[n] < b[n]) return -1;  // a[n]이 앞에 와야 하면 음수 반환

        // 2. 만약 n번째 글자가 같다면? (함정 해결)
        // 단어 전체를 사전순으로 비교합니다.
        if (a[n] === b[n]) {
            if (a > b) return 1;
            if (a < b) return -1;
        }

        return 0; // 값이 같으면 순서를 바꾸지 않음
    });

    // sort()는 원본을 변경하므로 정렬된 strings를 그대로 반환합니다.
    return strings;
}


// 남이 한 코드 - 간단 버전
function solution(strings, n) {
    return strings.sort((a, b) => {
        // n번째 글자가 다르면 글자 비교, 같으면 단어 전체 비교
        return a[n] === b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n]);
    });
}
