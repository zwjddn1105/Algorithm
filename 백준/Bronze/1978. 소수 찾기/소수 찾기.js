const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const [n, input] = fs.readFileSync(filePath).toString().trim().split("\n")

let nums = input.split(" ").map(Number)


let cnt = 0

for (let i = 0; i < n; i++) {
  let isPrime = true
  if (nums[i] === 1) {
    isPrime = false
    continue
  }

  for (let j = 2; j < nums[i]; j++) {
    if (nums[i] % j === 0) {
      isPrime = false
      break
    }
  }
  if (isPrime) {
    cnt += 1
  }
}
console.log(cnt)
