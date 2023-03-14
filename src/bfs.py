from queue import Queue
import sys


def read():
    with open(INPUT, 'r') as f:
        rows, cols = int(f.readline()), int(f.readline())
        graph = {}
        for i in range(1, rows+1):
            line = f.readline().split()
            for j, state in enumerate(line):
                if state == '0':
                    node = Node((i, j+1))
                    graph[i, j+1] = node
        x, y = f.readline().split()
        start = int(x), int(y)
        x, y = f.readline().split()
        end = int(x), int(y)
    return graph, start, end


class Node:
    def __init__(self, cell):
        self.vertex = cell
        self.parent = None


def find_path(graph: dict, start: Node, end: Node):
    queue = Queue()
    visited = set()
    queue.put(start)
    first_time = True
    stop = False
    while not stop and not queue.empty() or first_time:
        first_time = False
        node = queue.get()
        visited.add(node)
        (x, y) = node.vertex
        for i in range(0, 3, 2):
            cell = x + i - 1, y
            if (cell in graph
                    and graph[cell] not in visited):
                graph[cell].parent = node
                if graph[cell] == end:
                    stop = True
                    break
                queue.put(graph[cell])

        for j in range(0, 3, 2):
            cell = x, y + j - 1
            if (cell in graph
                    and graph[cell] not in visited):
                graph[cell].parent = node
                if graph[cell] == end:
                    stop = True
                    break
                queue.put(graph[cell])

    if end.parent is None:
        return []

    result = [end]
    current = end
    while current.parent is not None:
        result.append(current.parent)
        current = current.parent
    result.reverse()
    return result


def write(result: list):
    with open(OUTPUT, 'w') as f:
        f.write("N\n" if len(result) == 0 else "Y\n")
        for node in result:
            x, y = node.vertex
            f.write(f"{x} {y}\n")


if __name__ == '__main__':
    INPUT = sys.argv[1]
    OUTPUT = sys.argv[2]
    graph, start, end = read()
    write(find_path(graph, graph[start], graph[end]))
