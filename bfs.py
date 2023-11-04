
def breadthfirstPrint(graph , start):
    queue = [ start ]


    while len(queue)>0:
        current = queue.pop(0)
        print(current, end=', ')

        for neighbour in graph[current]:
            queue.append(neighbour)



graph = {'a' : ('b' , 'c'),
         'b' : ('d'),
         'c' : ('e'),
         'd' : ('f'),
         'e' : (),
         'f' : ()}

breadthfirstPrint(graph , 'a')
