const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const [...input] = fs.readFileSync(filePath).toString().trim().split(" ").map(Number)

let [a, b] = input

if (a > b) {
  console.log(">")
} else if (a < b) {
  console.log("<")
} else {
  console.log("==")
}
