'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import heapq
def prims(graph,start):
    visited=set()
    
    parent=[]
    n=len(graph)-1
    for i in range(n+1):
        parent.append(-1)
        
    min_heap=[]
    heapq.heappush(min_heap,(0,start))
    
    mst_cost=0
    mst_edge=[]
    
    while min_heap:
        w,u=heapq.heappop(min_heap)
        
        if u in visited:
            continue
        
        visited.add(u)
        mst_cost+=w
        
        if parent[u]!=-1:
            mst_edge.append((parent[u],u,w))
        
        for v,wt in graph[u]:
            if v not in visited:
                parent[v]=u
                heapq.heappush(min_heap,(wt,v))
                
    return mst_cost,mst_edge
    
n=int(input("Enter the no of vertices :"))
m=int(input("Enter the no of edges :"))

graph=[]

for i in range(n+1):
    graph.append([])

for i in range(m):
    u,v,w=map(int,input("Enter the eges u,v and weight w :").split())
        
    graph[u].append((v,w))
    graph[v].append((u,w))
    
start=int(input("Enter the starting node :"))

min_cst,min_edges=prims(graph,start)
for u,v,w in min_edges:
    print(f'edge {u}-{v} and weight is {w}')
print("The min code is ",min_cst)
        
