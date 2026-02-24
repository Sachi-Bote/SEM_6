def bfs_recursive(adj, queue, visited, n):
    if not queue:   # base condition
        return

    node = queue.pop(0)
    print(node, end=" ")

    # check all neighbours using adjacency matrix
    for i in range(n):
        if adj[node][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)

    bfs_recursive(adj, queue, visited, n)


# ---------------- MAIN ----------------
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
adj = []
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

start = int(input("Enter starting vertex: "))

visited = [False] * n
queue = []

visited[start] = True
queue.append(start)

print("\nBFS Traversal:")
bfs_recursive(adj, queue, visited, n)
print()

