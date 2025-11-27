'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def dfs(graph,start,visited=None):
    if visited==None:
        visited=set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
        
    
    
n=int(input("Enter the size of graph:"))
graph={}
for i in range(n):
    u,v=input("Enter edge u,v:").split()
    u=int(u)
    v=int(v)
    
    if u not in graph:
        graph[u]=[]
        
    if v not in graph:
        graph[v]=[]
        
    graph[u].append(v)
    graph[v].append(u)
    
start=int(input("Enter start node :"))

print("Dfs traversal of graph is :")
visited=set()
dfs(graph,start,visited)
if len(visited)==n:   # if there is no connected graph then the size of graph and the size of the set will be same
    print("There is a cycle")
else:
    print("There is no cycle")
