import graph_info

def bfs(graph, start, goal):
    queue = [[start]]; # contains paths, like this: S => D => G , S => A , ... etc
    visited = [];

    while queue:
        print("Current Queue: ", queue);
        path = queue.pop(0) # removes the first element, because this is a queue
        node = path[-1] # get the last node of the path

        if node in visited:
            continue;

        visited.append(node);

        if node == goal:
            return path;
        else:
            adj_nodes = graph.get(node, []); # gets all neighbours of the node, if it doesn't have neighbours, it will return empty list []

            for adj in adj_nodes:
                if adj not in path: # path already contains the node, then ignore it
                    new_path = list(path); # create new copy of the current path
                    new_path.append(adj); # then add the new node to it
                    queue.append(new_path); # then add it to the queue

solution = bfs(graph_info.graph, 'S', 'G');
print(solution);
