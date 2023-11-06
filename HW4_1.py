import heapq
from scipy.io import loadmat

# Define the priority queue class using heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}  # mapping of nodes to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        self.counter = 0  # unique sequence count

    def insert(self, node, priority):
        if node in self.entry_finder:
            self.remove(node)
        count = self.counter
        self.counter += 1
        entry = [priority, count, node]
        self.entry_finder[node] = entry
        heapq.heappush(self.heap, entry)

    def remove(self, node):
        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED  # Assign a placeholder for a removed task

    def extract_min(self):
        while self.heap:
            priority, count, node = heapq.heappop(self.heap)
            if node != self.REMOVED:
                del self.entry_finder[node]
                return node
        raise KeyError('pop from an empty priority queue')

    def decrease_key(self, node, priority):
        # This will remove the node and re-insert it with the updated priority
        self.remove(node)
        self.insert(node, priority)

    def is_empty(self):
        return not self.entry_finder


# Dijkstra's algorithm implementation in Python
def myDijkstra(adj_matrix, origin):
    num_nodes = len(adj_matrix)
    dist = [float('inf')] * num_nodes
    prev = [-1] * num_nodes
    dist[origin] = 0
    
    pq = PriorityQueue()
    for node in range(num_nodes):
        pq.insert(node, dist[node])
    
    while not pq.is_empty():
        u = pq.extract_min()
        for v, weight in enumerate(adj_matrix[u]):
            if weight > 0 and weight != "inf":  # There is an edge
                alt = dist[u] + weight
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    pq.decrease_key(v, alt)
    
    return dist, prev

# Load and process each graph
num_graphs = 6

for graph_num in range(1, num_graphs + 1):
    # Load the graph data from the MAT file
    file_name = f'graph{graph_num}.mat'
    mat_data = loadmat(file_name)
    adj_matrix = mat_data[f'graph{graph_num}']
    
    # Convert MATLAB 1-indexing to Python 0-indexing
    
    origin = 0  # Specify the origin node (starting node)
    
    # Call Dijkstra's algorithm
    dist, prev = myDijkstra(adj_matrix, origin)
    prev=[i+1 for i in prev]
    
    # Display the results
    print(f'Table {graph_num}: {file_name}')
    print('dist prev')
    for i, (d, p) in enumerate(zip(dist, prev)):
        print(f'{d} {p}')
    print()
