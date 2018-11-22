from collections import namedtuple, defaultdict

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, weight')


def node_equal(li):
    element = li[0][0]
    for l in range(len(li)):
        if li[l][0] == element:
            continue
        else:
            return False
    return True


def get_edges_from_file(file_name):
    with open(file_name) as file_obj:
        lines = file_obj.readlines()

    edge_list = []
    for idx in range(2, len(lines)):
        current_line = lines[idx].split()
        current_line = list(map(int, current_line))
        start = current_line[0]
        end = current_line[1]
        latency = current_line[2]
        edge = Edge(start, end, latency)
        edge_list.append(edge)

    return edge_list


def get_clients_from_file(file_name):
    with open(file_name) as file_obj:
        lines = file_obj.readlines()

    clients = lines[1].split()
    # converting to int
    clients = list(map(int, clients))

    return clients


def get_routers(edges, clients):
    vertices = set(e[0] for e in edges) | set(e[1] for e in edges)
    return vertices.difference(set(clients))


def get_dist(edges, start):
    visited = []

    vertices = set(e[0] for e in edges) | set(e[1] for e in edges)
    dist_to = {v: inf for v in vertices}
    dist_to[start] = 0

    while set(visited) != set(vertices):
        current_node = start
        dist_copy = dist_to.copy()
        while current_node in visited:
            current_node = min(dist_copy, key=dist_to.get)
            del dist_copy[current_node]
        working_edges = []
        for begin, end, weight in edges:
            if begin == current_node: working_edges.append(Edge(begin, end, weight))
            if end == current_node: working_edges.append(Edge(end, begin, weight))

        for edge in working_edges:
            if dist_to[edge.end] > dist_to[current_node] + edge.weight:
                dist_to[edge.end] = dist_to[current_node] + edge.weight
        visited.append(current_node)

    return dist_to


def solve(file_name):
    edges = get_edges_from_file(file_name)
    clients = get_clients_from_file(file_name)

    distances = defaultdict(dict)
    for client in clients:
        distances[client] = get_dist(edges, client)

        for client, dist_to in distances.items():
            distances[client] = [(k, dist_to[k]) for k in sorted(dist_to, key=dist_to.get)
            if k not in clients]

    equal = False
    check_list = []
    count = 0
    while not equal:
        count += 1
        min_dist = (inf, inf)
        for idx, (client, dists) in enumerate(distances.items()):
            if count == 1:
                check_list.append(dists.pop(0))
            else:
                if len(dists) != 0 and min_dist[1] > dists[0][1]:
                    min_dist = dists[0]
                    place = idx
                    current_client = client

        if count > 1 and distances[current_client]:
            check_list[place] = min_dist
            distances[current_client].pop(0)
        equal = node_equal(check_list)

    return check_list


if __name__ == "__main__":
    res = solve('gamsrv.in')
    print(res)
    maximum = max(res, key=lambda item: item[1])[1]
    print(maximum)