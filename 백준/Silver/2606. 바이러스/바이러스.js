const readline = require("readline")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []

rl.on("line", (line) => {
  input.push(line)
}).on("close", () => {
  // 입력 처리
  const n = parseInt(input[0]) // 첫째 줄: 컴퓨터 수
  const edgeCount = parseInt(input[1]) // 둘째 줄: 연결된 컴퓨터 쌍의 수
  const connections = input.slice(2).map((line) => line.split(" ").map(Number)) // 연결 정보

  // 알고리즘 실행
  const result = countInfectedComputers(n, connections)
  console.log(result)

  process.exit()
})

function countInfectedComputers(n, connections) {
  // 인접 리스트 생성
  const graph = Array.from({ length: n + 1 }, () => [])
  connections.forEach(([a, b]) => {
    graph[a].push(b)
    graph[b].push(a)
  })

  // BFS 탐색
  const visited = Array(n + 1).fill(false)
  const queue = [1] // 1번 컴퓨터부터 시작
  visited[1] = true

  let infectedCount = 0

  while (queue.length > 0) {
    const current = queue.shift() // 큐에서 컴퓨터 꺼내기

    for (const neighbor of graph[current]) {
      if (!visited[neighbor]) {
        visited[neighbor] = true
        queue.push(neighbor)
        infectedCount++
      }
    }
  }

  return infectedCount
}
