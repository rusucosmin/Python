#~/usr/bin/python

def dfs(graph, node, used, con):
	used[node] = True
	con.append(node)
	for it in graph[node]:
		if used[it] == False:
			dfs(graph, it, used, con)

def main():
	n = int(input())
	m = int(input())
	visited = [False for i in range(1, n + 2)]
	graph = dict((key, []) for key in range(1, n + 2))
	for i in range (1, m + 1):
		x = int(input())
		y = int(input())
		graph[x].append(y)
		graph[y].append(x)
	conexcomp = {}
	size = -1
	for i in range(1, n + 1):
		print i
		if visited[i] == False:
			con = []
			dfs(graph, i, visited, con)
			size += 1;
			conexcomp[size] = con
	print conexcomp
			

if __name__ == '__main__':
	main()
