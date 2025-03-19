const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
let input = fs.readFileSync(filePath).toString().trim()

input = input.split(" ").map(Number)

const a = parseInt(input[0])
const b = parseInt(input[1])

let answer = a / b
console.log(answer)
