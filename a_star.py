import graph_info

def path_f_cost(path, h_table):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = h_table[last_node]
    f_cost = g_cost + h_cost
    return f_cost, last_node

def a_star(graph, start, end, h_table):
    queue = [[(start, 0)]];
    visited = [];
    
    while queue:
        queue.sort(key=lambda x: path_f_cost(x, h_table))
        path = queue.pop(0)
        node = path[-1][0]

        if node in visited:
            continue
        visited.append(node)

        if node == end:
            return path
        else:
            for (adj, cost) in graph[node]:
                new_path = path.copy()
                new_path.append((adj, cost))
                queue.append(new_path)

solution = a_star(graph_info.weighted_graph, 'S', 'G', graph_info.H_table)
print('Solution is:', solution)
print('Cost of solution is:', path_f_cost(solution, graph_info.H_table)[0])
