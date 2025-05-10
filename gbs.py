import graph_info

def path_cost(path, h_table):
    return h_table[path[-1][0]]

def gbs (graph, start, goal, h_table):
    queue = [[(start, 0)]] # contains paths with costs, like this: (S, 0) => (D, 5) => (G, 6) ... etc
    visited = []

    while queue:
        print("Current Queue: ", queue);
        queue.sort(key = lambda x: path_cost(x, h_table)) # sorts the queue according to the least path cost, which we calculate using the h_table only
        path = queue.pop(0) # removes the first element, because this is a queue
        node = path[-1][0] # get the last node of the path, then get its letter node

        if node in visited:
            continue

        if node == goal:
            return path
        else:
            adj_nodes = graph.get(node, []); # gets all neighbours of the node, if it doesn't have neighbours, it will return empty list []
            for (adj, cost) in adj_nodes:
                # note that we don't have to check if adj is in path, because the path is already sorted
                new_path = list(path); # create new copy of the current path
                new_path.append((adj, cost)); # then add the new node to it
                queue.append(new_path); # then add it to the queue

def path_total_cost(path):
    return sum(cost for (node, cost) in path)

solution = gbs(graph_info.weighted_graph, 'S', 'G', graph_info.H_table)
print('Solution is:', solution)
print('Cost of solution is:', path_total_cost(solution))
