const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let result = input[0] * input[1] * input[2];

result = String(result);
const obj = {};

for (let i = 0; i < 10; i++) {
  obj[i] = 0;
}
for (let i = 0; i < result.length; i++) {
  let num = Number(result[i]);
  obj[num] += 1;
}

for (let i = 0; i < 10; i++) {
  console.log(obj[i]);
}
