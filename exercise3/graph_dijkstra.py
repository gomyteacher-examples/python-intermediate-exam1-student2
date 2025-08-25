import heapq
from collections import defaultdict

class Graph:
    """Graph class for shortest paths"""
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v, weight):
        """Add edge to graph"""
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
        return self  # method chaining
    
    @classmethod
    def from_adjacency_list(cls, adj_list):
        """Build graph from adjacency list - copied from example"""
        graph = cls()
        for vertex, edges in adj_list.items():
            for neighbor, weight in edges:
                graph.add_edge(vertex, neighbor, weight)
        return graph
    
    def dijkstra(self, start, end):
        """Find shortest path using dijkstra algorithm"""
        # basic dijkstra with path tracking
        distances = {vertex: float('infinity') for vertex in self.vertices}
        previous = {}  # track path
        distances[start] = 0
        
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue
                
            visited.add(current_vertex)
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
        
        # build path - hope this works
        path = []
        current = end
        while current in previous:
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()
        
        return distances[end], path
    
    def __str__(self):
        return f"Graph with {len(self.vertices)} vertices"

if __name__ == "__main__":
    # test with the exam example
    g = Graph.from_adjacency_list({
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)]
    })
    
    distance, path = g.dijkstra('A', 'E')
    print(f"Shortest distance: {distance}, Path: {' -> '.join(path)}")
    
    # test method chaining 
    g2 = Graph().add_edge('X', 'Y', 3).add_edge('Y', 'Z', 2)
    print(f"Graph 2: {g2}")
    
    # basic test
    dist2, path2 = g2.dijkstra('X', 'Z')
    print(f"X to Z: distance={dist2}, path={path2}")
