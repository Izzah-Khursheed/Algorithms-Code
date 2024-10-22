graph = { 
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['G'],
    'E' : [],
    'F' : ['H'],
    'G' : [],
    'H' : []
}

def bfs(graph, start, goal):
    if not graph:
        print ("Fail")
        return 
    queue = [start]
    visited = set()
    queue_path = []

    while queue:
        node = queue.pop(0)
        visited.add(node)
        queue_path.append(node)
        if node == goal:
            print("Following is the path of Breadth First Search:")
            print(queue_path)
            print ("True")
            return 

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    print("Goal node not found in the graph.")
    print("False") 
    
bfs(graph, 'A', 'H')
