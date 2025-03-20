const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const n = fs.readFileSync(filePath).toString().trim();

let star = Number(n);

for (let i = 0; i <= star - 1; i++) {
  process.stdout.write(" ".repeat(n - i - 1));
  process.stdout.write("*".repeat(i + 1));
  process.stdout.write("\n");
}
