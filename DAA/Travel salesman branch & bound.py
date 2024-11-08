import sys

class TSP:
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph
        self.min_cost = sys.maxsize

    def tsp_branch_and_bound(self):
        visited = [False] * self.n
        visited[0] = True
        self._branch_and_bound(0, 1, 0, visited)
        return self.min_cost

    def _branch_and_bound(self, curr_city, level, curr_cost, visited):
        if level == self.n:
            if self.graph[curr_city][0] != 0:
                self.min_cost = min(self.min_cost, curr_cost + self.graph[curr_city][0])
            return

        for i in range(self.n):
            if not visited[i] and self.graph[curr_city][i] != 0:
                visited[i] = True
                self._branch_and_bound(i, level + 1, curr_cost + self.graph[curr_city][i], visited)
                visited[i] = False

def get_graph_input():
    n = int(input("Enter the number of cities: "))
    print(f"Enter the distance matrix for {n} cities (use space-separated values for each row):")
    
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Enter distances from city {i + 1} to all cities (including itself): ").split()))
        if len(row) != n:
            raise ValueError("Each row must have the same number of elements as the number of cities.")
        graph.append(row)
    
    return n, graph

if __name__ == "__main__":
    try:
        n, graph = get_graph_input()
        tsp_solver = TSP(n, graph)
        min_cost = tsp_solver.tsp_branch_and_bound()
        print(f"\nMinimum cost of TSP: {min_cost}")
    except ValueError as e:
        print(f"Invalid input: {e}")

