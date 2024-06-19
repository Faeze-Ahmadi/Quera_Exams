import heapq

def dijkstra(graph, start):
    n = len(graph)
    
    distances = {node: float('inf') for node in range(n)}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

graph = {
    0: {1: 2, 2: 4},
    1: {2: 1, 3: 7},
    2: {3: 3},
    3: {}
}

start_vertex = 0
distances = dijkstra(graph, start_vertex)

print(f"Distance:{start_vertex}: {distances}")
