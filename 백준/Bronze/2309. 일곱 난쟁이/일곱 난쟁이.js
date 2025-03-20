const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);

let total = 0;
for (let i = 0; i <= 8; i++) {
  total += input[i];
}

for (let i = 0; i <= 8; i++) {
  let isFind = false;
  for (let j = i + 1; j <= 8; j++) {
    let sum = total;
    sum -= input[i] + input[j];
    if (sum === 100) {
      input = input.filter((item, index, arr) => {
        return item !== input[i] && item !== input[j];
      });
      isFind = true;
      break;
    }
  }
  if (isFind) {
    break;
  }
}

input.sort((a, b) => {
  return a - b;
});

for (let i = 0; i <= 6; i++) {
  console.log(input[i]);
}
