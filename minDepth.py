import threading
import queue

thisdict = {
    1: [2, 3],
    2: [4, 5],
    4: None,
    5: None,
    3: [6, 7],
    6: None,
    7: [8]
}


def minDepth(graph):
    q = queue.Queue()
    root = graph[1]
    for x in graph[1]:
        q.put(graph[x])
