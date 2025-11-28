'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def knapsack(value,weight,capacity):
    n=len(value)
    ratio=[]
    for i in range(n):
        r=value[i]/weight[i]
        ratio.append((r,value[i],weight[i])) # here we are storing both ratio and total value bcz if capacity is more than total weight then we can take that item or else only ratio
    
    ratio.sort(reverse=True)
    total_value=0
    knapsack_item=[]
    for r,v,w in ratio:
        if capacity>=w:
            capacity=capacity-w
            total_value+=v
            knapsack_item.append((v,w))
        else:
            total_value+=r*capacity # here we are taking fractional part of knapsack not the total as the weight is more than capacity
            knapsack_item.append((r*capacity,capacity))
            break
        
    return total_value
            
        
n=int(input("Enter no of items :"))
capacity=int(input("Enter capacity of knapsack :"))

value=[]
weight=[]

print("Enter weight and value of knapsack :")
for i in range(n):
    v=int(input(f"Enter the value of {i+1} item :"))
    w=int(input(f"Enter the weight of {i+1} item :"))
    value.append(v)
    weight.append(w)
    
print("Maximum value is :")
print(knapsack(value,weight,capacity))
    
    
