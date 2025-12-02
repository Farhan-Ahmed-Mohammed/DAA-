'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def warshell(graph):
    n=len(graph)
    clouser=[]
    
    for i in range(n):
        new_r=[]
        for j in range(n):
            new_r.append(graph[i][j])
        clouser.append(new_r)
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                clouser[i][j]=clouser[i][j] or (clouser[i][k] and clouser[k][j])
    
    return clouser
    
    
n=int(input("Enter the size of graph :"))
graph=[]

print("Enter the adjacency matrix(0/1):")
for i in range(n):
    row=list(map(int,input().split()))
    graph.append(row)
    
clouser=warshell(graph)

print("The transitive clouser is :")
for row in clouser:
    print(*row)
