import graph_info

def path_cost(path, graph):
    return sum(cost for (node, cost) in path), path[-1][0]

def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]] # contains paths with costs, like this: (S, 0) => (D, 5) => (G, 6) ... etc

    while queue:
        print("Current Queue: ", queue);
        queue.sort(key = lambda x: path_cost(x, graph)) # sorts the queue according to the least path cost, which we calculate by summing the costs of all nodes of the path
        path = queue.pop(0) # removes the first element, because this is a queue
        node = path[-1][0] # get the last node of the path, then get its letter node

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return path
        else:
            adj_nodes = graph.get(node, []); # gets all neighbours of the node, if it doesn't have neighbours, it will return empty list []
            for (adj, cost) in adj_nodes:
                if adj not in path: # path already contains the node, then ignore it
                    new_path = list(path); # create new copy of the current path
                    new_path.append((adj, cost)); # then add the new node to it
                    queue.append(new_path); # then add it to the queue


solution = ucs(graph_info.weighted_graph, 'S', 'G')
print('Solution is', solution)
print('Cost of Solution is', path_cost(solution, graph_info.weighted_graph)[0])

