const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let max_num = 0;

max_num = Math.max(...input);
console.log(max_num);

console.log(input.indexOf(max_num) + 1);
