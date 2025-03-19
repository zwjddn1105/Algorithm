const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
let input = fs.readFileSync(filePath).toString().trim()

input = input.split(" ").map(Number)

const a = input[0]
const b = input[1]
let answer = a - b
console.log(answer)
