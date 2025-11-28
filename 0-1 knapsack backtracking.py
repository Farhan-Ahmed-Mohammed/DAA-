'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def back(value,weight,capacity,index,curr_value):
    global max_value
    if index==len(value) or capacity<=0:
        max_value=max(max_value,curr_value)
        return
    
    if capacity>=weight[index]: #including 
        back(value,weight,capacity-weight[index],index+1,curr_value+value[index])
    
    back(value,weight,capacity,index+1,curr_value) #excluding
    
n=int(input("Enter no of items:"))
capacity=int(input("Enter the capacity of knapsack :"))

value=[]
weight=[]

for i in range(n):
    v=int(input(f"Enter the value of item{i+1}:"))
    w=int(input(f"Enter the weight of item{i+1}:"))
    value.append(v)
    weight.append(w)
    
max_value=0
print("The maximum value in knapsack is :")
back(value,weight,capacity,0,0)
print(max_value)
