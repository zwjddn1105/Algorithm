const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);
const n = input[0];
const k = input[1];
let nums = [];
let len = 0;
let isFind = false;

for (let i = 1; i <= n; i++) {
  if (n % i === 0) {
    nums.push(i);
    len += 1;
    if (len === k) {
      isFind = true;
      break;
    }
  }
}
if (isFind) {
  console.log(nums.at(-1));
} else {
  console.log(0);
}
