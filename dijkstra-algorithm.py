import heapq

def dijkstra(graph, start):
    # تعداد رئوس گراف
    n = len(graph)
    
    # فاصله از راس شروع به سایر رئوس
    distances = {node: float('inf') for node in range(n)}
    distances[start] = 0
    
    # صف اولویت برای رئوس
    priority_queue = [(0, start)]
    
    while priority_queue:
        # استخراج راس با کمترین فاصله موقتی
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # بررسی همسایه‌ها
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # اگر فاصله جدید کمتر از فاصله قبلی است، آن را به روز رسانی کن
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# تعریف گراف به صورت دیکشنری از دیکشنری‌ها
# مثال گراف:
# گراف به صورت لیست مجاورتی: گراف {0: {1: 2, 2: 4}, 1: {2: 1, 3: 7}, 2: {3: 3}, 3: {}}
graph = {
    0: {1: 2, 2: 4},
    1: {2: 1, 3: 7},
    2: {3: 3},
    3: {}
}

# اجرای الگوریتم از راس 0
start_vertex = 0
distances = dijkstra(graph, start_vertex)

print(f"فاصله‌ها از راس {start_vertex}: {distances}")
