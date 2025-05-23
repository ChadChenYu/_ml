import random
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(route, cities):
    return sum(distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1)) + distance(cities[route[-1]], cities[route[0]])

def get_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(cities, max_iterations=1000):
    num_cities = len(cities)
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_distance = total_distance(current_route, cities)
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current_route)
        best_neighbor = min(neighbors, key=lambda route: total_distance(route, cities))
        best_neighbor_distance = total_distance(best_neighbor, cities)
        
        if best_neighbor_distance < current_distance:
            current_route, current_distance = best_neighbor, best_neighbor_distance
        else:
            break
    
    return current_route, current_distance

# 測試
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
best_route, best_distance = hill_climbing(cities)
print("Best Route:", best_route)
print("Best Distance:", best_distance)
# 採用GPT生成
https://chatgpt.com/canvas/shared/67cf010e67dc8191964e7202e204bbdf
