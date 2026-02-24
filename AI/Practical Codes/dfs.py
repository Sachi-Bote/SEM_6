def dfs_recursive(adj, node, visited, n):
    visited[node] = True
    print(node, end=" ")

    # check all neighbours
    for i in range(n):
        if adj[node][i] == 1 and not visited[i]:
            dfs_recursive(adj, i, visited, n)


# ---------------- MAIN ----------------
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
adj = []
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

start = int(input("Enter starting vertex: "))

visited = [False] * n

print("\nDFS Traversal:")
dfs_recursive(adj, start, visited, n)
print()

