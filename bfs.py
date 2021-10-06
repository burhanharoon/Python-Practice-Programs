def bfs(graph, explored, toFind):
    find = False
    for node in graph:
        for i in range(2):
            # print(graph[node][i])
            if toFind in graph[node][i]:
                print(toFind)
                find = True
                break
            else:
                find
                pass
    if find:
        print('ok')
    else:
        print("Node not found")


graph = {
    '0': ['a', 'b'],
    '1': ['c', 'd'],
    '2': ['e', 'f'],
    '3': ['g', 'h'],
    '4': ['i', 'j']
}

explored = []
bfs(graph, explored, 'ii')

# print(graph)
