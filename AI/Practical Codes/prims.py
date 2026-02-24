#Implement Greedy Search Algorithm for any of the following application
#2.Prims Algorithm

INF = 99999

def input_graph():
	n = int(input("Enter the number of vertices: "))
	print("Enter the adjacency matrix (0 if no edges)")
	
	graph = []
	for i in range (n):
		row = list(map(int, input().split()))
		graph.append(row)
		
	return graph, n
	


def prim_mst(graph, n):
	selected = [0]*n
	selected[0] = 1
	
	edges = 0
	total_cost = 0
	
	print("\n Edge: Weight")
	
	while edges < n -1:
		minimum = INF
		x = 0
		y = 0
		
		for i in range(n):
			if(selected[i] == 1):
				for j in range(n):
					if (selected[i] ==0 and graph[i][j] !=0):
						if (graph[i][j] < minimum):
							minimum = graph[i][j]
							x=i
							y=j
						
		print(x, "-", y, ";", graph[x][y])
		total_cost += graph[x][y]
		selected[y] =1
		edges += 1
		
	print("Total Cost of MST: ", total_cost)
	
graph, n = input_graph()
prim_mst(graph, n)
	
	
	
