const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const n = 10;
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let person = 0;
let answer = 0;
for (let i = 0; i <= n - 1; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  person -= a;
  answer = Math.max(person, answer);
  person += b;
  answer = Math.max(person, answer);
}

// process.stdout.write(answer); 문자열 출력함수라 안됨
console.log(answer);
