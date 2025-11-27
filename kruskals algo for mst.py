'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def find(parent,x):
    while parent[x]!=x:
        x=parent[x] #it means we are moving upwards to get parent now we are checking like parent[parent[x]] like that till we reach the top parent where  parent of top node is it self
    return x
    
def union(parent,x,y):
    xp=find(parent,x)
    yp=find(parent,y)
    if xp!=yp:   # if both are equal means cycle exists
        parent[yp]=xp # it means we are joining them and then y s parent is x now
        return True
    return False
    
n=int(input("Enter no of vetrices :"))
m=int(input("Enter no of edges :"))

edges=[]

for i in range(m):
    u,v,w=input("Enter u,v,w :").split()
    u=int(u)
    v=int(v)
    w=int(w)
    
    edges.append((w,u,v)) # w first bcz wrt to w we have to sort
    
edges.sort()

parent=[]
for i in range(n+1):
    parent.append(i)
    
mst_cost=0
mst_edges=[]

for w,u,v in edges:
    if union(parent,u,v):
        mst_cost+=w
        mst_edges.append((u,v,w))

print("MST:")
for u,v,w in mst_edges:
    print(f'Edge {u}-{v} weight={w}')
    
print("Total cose:",mst_cost)
    


    
