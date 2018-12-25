#queue operations

def find_path(graph,start,end):
    queue =list()
    ident  = {}
    for k in graph.keys():
        ident[k] =""
    queue.append(start)
    visited = []
    steps = 0
    find = False
    while(len(queue)>0):
        node = queue[0]
        print(queue)
        if end in graph[node]:
            find = True
            break;
        for i in graph[node]:
            if i not in visited:
                queue.append(i)
                ident[i] = node
        visited.append(queue.pop(0))
    if find:
        path = [node]
        fol =''
        while fol != start:
            fol = ident[node]
            node = fol
            path.append(fol)
        return path
    else:
        return 0
        
graph ={ 
'a':['c','d'], 
'b':['d'], 
'c':['a'], 
'd':['e', 'b'], 
'e':['b', 'c'] 
} 
path = find_path(graph,'b','a')
print("final :",path)
