Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import heapq

def my_dijkstra(adj_matrix, origin):
    num_nodes = len(adj_matrix)
    
    # Initialize dist and prev arrays
    dist = [float('inf')] * num_nodes
    prev = [None] * num_nodes
    
    # Initialize the distance to the origin node as 0
    dist[origin] = 0
    
    # Create a priority queue and insert all nodes with their distances
    pq = [(0, origin)]  # Priority queue as a list of tuples (distance, node)
    visited = set()  # Set to keep track of visited nodes
    
    while pq:
        # Extract the node with the minimum distance
        u_dist, u = heapq.heappop(pq)
...         
...         if u in visited:
...             continue
...         
...         visited.add(u)
...         
...         # Explore neighbors of u
...         for v, weight in enumerate(adj_matrix[u]):
...             if weight > 0 and v not in visited:  # Check if there is an edge and v is unvisited
...                 alt = u_dist + weight  # Calculate the potential new distance
...                 if alt < dist[v]:  # If the new distance is shorter, update it
...                     dist[v] = alt
...                     prev[v] = u
...                     heapq.heappush(pq, (alt, v))  # Update the priority queue
...     
...     # Set dist to infinity for unreachable nodes
...     dist = [d if d != float('inf') else float('inf') for d in dist]
...     
...     # Adjust prev to be 0-indexed
...     prev = [p if p is None else p + 1 for p in prev]
...     prev[origin] = origin
...     
...     return dist, prev
