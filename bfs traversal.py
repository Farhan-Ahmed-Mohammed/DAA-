from collections import deque # here deque means double ended queue

def bfs(graph,start):
    visited=set()
    queue=deque([start]) #now start also acts like a queue as we have put it in deque([]) if we put start in [] it acts like lsit
    while queue:
        node=queue.popleft() # at start only 1 element but in next for loop all of the start neighbours are going to be added in queue so we use popleft to get FIFO order
        
        if node not in visited:
            print(node)
            visited.add(node)
            
            for neighbour in graph[node]: # graph[a]: b,c,d it gives all the element which are its neighbours 
                if neighbour not in visited:
                    queue.append(neighbour)
                    
graph={}
num=int(input("Enter the number of nodes :"))

for i in range(num):
    #for integers :u,v=map(int,input("Enter the edge u,v:").split())
    u,v=input("Enter the edge u,v:").split()
    if u not in graph:
        graph[u]=[]
        
    if v not in graph:
        graph[v]=[]
        
    graph[u].append(v)
    graph[v].append(u)
    
start=input("Enter the start node :")
print("BFS Traversal :")
bfs(graph,start)
