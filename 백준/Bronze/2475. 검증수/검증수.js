const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let sum = 0;
for (let i = 0; i <= 4; i++) {
  sum += input[i] ** 2;
}

let answer = 0;
answer = sum % 10;
console.log(answer);
