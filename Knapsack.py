def knapsack_tabulation(items,weights, values, capacity):      #defining the knapsack function
    n=items
    table = []
    for i in range(n + 1):      #creating a 2D list of n rows and capacity number of columns
        row = [0] * (capacity + 1)
        table.append(row)

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                include_item = values[i-1] + table[i-1][w-weights[i-1]]
                exclude_item = table[i-1][w]
                table[i][w] = max(include_item, exclude_item)
            else:
                table[i][w] = table[i-1][w]
    
    items_selected=[]
    w = capacity

    for i in range(n,0,-1):
        if table[i][w] != table[i-1][w]:
            items_selected.append(i)
            w = w-weights[i-1]

    for row in table:
    	  print(row)


    return table[n][capacity],items_selected[::-1]



items = int(input("Enter the total number of items : ")) #Taking total number of items from user
values = [] #creating list of Values
weights = [] #creating list of Weights

for i in range (items):
    weigh = int(input(f"Enter weight of item {i + 1}: "))    #Taking the weight of item from user one by one
    value = int(input(f"Enter value of item {i + 1}: "))     #Taking the value of item from user one by one
    weights.append(weigh)   #appending the new weights in the list
    values.append(value)    #appending the new values in the list


capacity = int(input("Enter the Capacity of the Cargo or Containeer: "))


Final_cost, items_selected = knapsack_tabulation( items,weights, values, capacity)     #calling the knapsack function to get the final cost and items to be selected

print("\nMaximum cost or value that can be obtained:", Final_cost)
print("\nItems to select:", items_selected)

