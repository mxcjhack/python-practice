
def depthfirstPrint(graph , start):
    stack = [ start ]


    while len(stack)>0:
        current = stack.pop()
        print(current, end=', ')

        for neighbour in graph[current]:
            stack.append(neighbour)


def depthfirstrecursive(graph , current):
    print(current)
    for neighbours in graph[current]:
        depthfirstrecursive(graph , neighbours)
            





graph = {'a' : ('b' , 'c'),
         'b' : ('d'),
         'c' : ('e'),
         'd' : ('f'),
         'e' : (),
         'f' : ()}

depthfirstPrint(graph , 'a')
print()
depthfirstrecursive(graph , 'a')