def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True  

    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c  

            if graph_coloring_util(graph, m, color, v + 1):  
                return True

            color[v] = 0  

    return False  

def graph_coloring(graph, m):
    color = [0] * len(graph)  

    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist.")
        return False

    print("Solution exists with the following color assignments:")
    for v in range(len(graph)):
        print(f"Vertex {v + 1} --> Color {color[v]}")  
    return True


if __name__ == "__main__":
    try:
        n = int(input("Enter the number of vertices in the graph: "))
        print("Enter the adjacency matrix (row by row, space-separated):")
        graph = []
        for _ in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                raise ValueError("Each row must have the same number of elements as the number of vertices.")
            graph.append(row)

        m = int(input("Enter the number of colors: "))
        if m < 1:
            print("The number of colors must be at least 1.")
        else:
            graph_coloring(graph, m)
    except ValueError as e:
        print(f"Invalid input: {e}")
