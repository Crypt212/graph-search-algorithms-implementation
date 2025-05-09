import graph_info

def bfs(graph, start, goal):
    stack = [[start]];
    visited = [];

    while stack:
        print("Current stack: ", stack);
        path = stack.pop(); # the exact same code of the bfs but you use just .pop() to remove the last element, because we are using stack here
        node = path[-1];

        if node in visited:
            continue;

        visited.append(node);

        if node == goal:
            return path;
        else:
            adj_nodes = graph.get(node, []);

            for adj in adj_nodes:
                if adj not in path:
                    new_path = list(path);
                    new_path.append(adj);
                    stack.append(new_path);

solution = bfs(graph_info.graph, 'S', 'G');
print(solution);
