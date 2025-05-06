from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

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
            items_selected.append(i-1)
            w = w-weights[i-1]

    return table[n][capacity],items_selected[::-1]


@app.route('/', methods=['GET', 'POST'])
def get_items():
    if request.method == 'POST':
        print(request.form)  # debug
        items = int(request.form['items']) 
        capacity = int(request.form['capacity'])
        return render_template('items.html', items=items, capacity=capacity)
    return render_template('index.html')

@app.route('/knapsack', methods=['POST'])
def knapsack():
    print("POST received at /knapsack") #debug
    print("Form data:", request.form) #debug
    items = int(request.form['items'])
    capacity = int(request.form['capacity'])
    values = [int(request.form[f'value{i}']) for i in range(items)]
    weights = [int(request.form[f'weight{i}']) for i in range(items)]
    print(request.form)
    result, selected_items = knapsack_tabulation(items, weights, values, capacity)
    return render_template('result.html', result=result, selected_items=selected_items)

# Run the app
if __name__ == '__main__':
    app.run(debug=True) 