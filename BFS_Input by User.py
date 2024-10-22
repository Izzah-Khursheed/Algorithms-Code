def bfs(graph, start_node, goal_node):
    if not graph:
        print ("Fail")
        return
    queue = [start_node]
    visited = set()
    queue_path = []

    while queue:
        node = queue.pop(0)
        visited.add(node)
        queue_path.append(node)
        if node == goal_node:
            print("Following is the path of Breadth First Search")
            print(queue_path)
            print ("True")
            return
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    print("Goal node not found in the graph")
    print("False") 

def get_graph():
    graph = {}
    while True:
        node = input("Enter a node (or 'done' to finish): ").strip()
        if node.lower() == 'done':
            break
        neighbors = input(f"Enter neighbors of {node} (comma-separated): ").strip().split(',')
        graph[node] = [n for n in neighbors]
    print (graph)      
    return graph


graph=get_graph()
start_node = input("Enter the starting node: ").strip()
goal_node = input("Enter the goal node: ").strip()
bfs(graph, start_node, goal_node)