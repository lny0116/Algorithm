process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);

    let star = '*';
    // console.log(star.repeat(a))
    // star.repeat(a);

    for (let i = 0; i < b; i++) {
        console.log(star.repeat(a))
    }
});