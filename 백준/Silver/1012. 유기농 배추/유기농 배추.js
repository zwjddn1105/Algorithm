const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [tc, ...input] = fs.readFileSync(filePath).toString().trim().split("\n");

let j = 0;
for (let testcase = 0; testcase <= tc - 1; testcase++) {
  let cnt = 0;
  let [m, n, k] = input[j].split(" ").map(Number);

  j += 1;

  let graph = Array.from({ length: n }, (value, idx) => {
    return Array(m).fill(0);
  });

  for (let i = 0; i <= k - 1; i++) {
    let [a, b] = input[j].split(" ").map(Number);
    graph[b][a] = 1;
    j += 1;
  }

  let visited = Array.from({ length: n }, (value, idx) => {
    return Array(m).fill(0);
  });

  const dx = [0, 0, 1, -1];
  const dy = [-1, 1, 0, 0];

  function dfs(i, j) {
    visited[i][j] = 1;
    for (let q = 0; q <= 3; q++) {
      let nx = i + dx[q];
      let ny = j + dy[q];
      if (
        0 <= nx &&
        nx < n &&
        0 <= ny &&
        ny < m &&
        visited[nx][ny] === 0 &&
        graph[nx][ny] === 1
      ) {
        dfs(nx, ny);
      }
    }
  }

  for (let i = 0; i <= n - 1; i++) {
    for (let j = 0; j <= m - 1; j++) {
      if (graph[i][j] === 1 && visited[i][j] === 0) {
        dfs(i, j);
        cnt += 1;
      }
    }
  }
  console.log(cnt);
}
