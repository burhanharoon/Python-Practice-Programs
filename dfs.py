stack = [1]

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: None,
    5: None,
    6: None,
    7: None,
}
keys = list(graph.keys())
goalNode = int(input("What's the goal node: "))

if keys.__contains__(goalNode):
    while(len(stack) != 0):
        elem = int(stack.pop())
        if elem == goalNode:
            print("Goal node found", elem)
            break
        else:
            if graph[elem] == None:
                continue
            else:
                length = graph[elem].__len__()
                for x in range(length, 0, -1):  # loop to push right to left child in stack
                    stack.append(graph[elem][x-1])

else:
    print("Bruh you writing a node that doesnt even eiest.")
