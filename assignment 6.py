
def greedy_by_profit(weights, values, capacity):
    n = len(weights)

    # Sort items according to profit (value) in descending order
    items = list(range(n))
    items.sort(key=lambda i: values[i], reverse=True)

    total_weight = 0
    total_value = 0
    selected = []

    for i in items:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            total_value += values[i]
            selected.append(i)

    return total_value, total_weight, selected

def greedy_by_weight(weights, values, capacity):
    n = len(weights)

    # Sort items according to weight in ascending order
    items = list(range(n))
    items.sort(key=lambda i: weights[i])

    total_weight = 0
    total_value = 0
    selected = []

    for i in items:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            total_value += values[i]
            selected.append(i)

    return total_value, total_weight, selected
def greedy_by_ratio(weights, values, capacity):
    n = len(weights)

    # Sort according to value/weight ratio in descending order
    items = list(range(n))
    items.sort(
        key=lambda i: values[i] / weights[i],
        reverse=True
    )

    total_weight = 0
    total_value = 0
    selected = []

    for i in items:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            total_value += values[i]
            selected.append(i)

    return total_value, total_weight, selected 
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # dp[i][w] = maximum value using first i items
    # with capacity w
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build the table
    for i in range(1, n + 1):
        item_weight = weights[i - 1]
        item_value = values[i - 1]

        for w in range(capacity + 1):

            # If item can fit
            if item_weight <= w:

                # Maximum of:
                # 1. Not taking the item
                # 2. Taking the item
                dp[i][w] = max(
                    dp[i - 1][w],
                    item_value + dp[i - 1][w - item_weight]
                )

            else:
                # Item cannot fit
                dp[i][w] = dp[i - 1][w]

  
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()

    total_value = dp[n][capacity]
    total_weight = sum(weights[i] for i in selected)

    return total_value, total_weight, selected, dp

def knapsack_top_down(weights, values, capacity):

    n = len(weights)

    # Memoization table
    memo = [[-1 for _ in range(capacity + 1)]
            for _ in range(n + 1)]

    
    def solve(i, w):

        # No items or no capacity
        if i == 0 or w == 0:
            return 0

        # Already calculated
        if memo[i][w] != -1:
            return memo[i][w]

        # Current item
        item_weight = weights[i - 1]
        item_value = values[i - 1]

        # If item is too heavy, don't take it
        if item_weight > w:

            memo[i][w] = solve(i - 1, w)

        else:

            # Don't take the item
            not_take = solve(i - 1, w)

            # Take the item
            take = item_value + solve(
                i - 1,
                w - item_weight
            )

            memo[i][w] = max(take, not_take)

        return memo[i][w]

    # Calculate maximum value
    total_value = solve(n, capacity)

   
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if memo[i][w] == -1:
            solve(i, w)

        if memo[i][w] != memo[i - 1][w]:

            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()

    total_weight = sum(weights[i] for i in selected)

    return total_value, total_weight, selected, memo
def display_result(method, value, weight, selected, weights, values):

    print("\n" + "=" * 60)
    print(method)
    print("=" * 60)

    print("Selected Items:", end=" ")

    if len(selected) == 0:
        print("None")
    else:
        for i in selected:
            print(f"Item {i + 1}", end=" ")
        print()

    print("Total Weight :", weight)
    print("Total Value  :", value)

    print("\nItem Details:")

    for i in selected:
        print(
            f"Item {i + 1} -> "
            f"Weight = {weights[i]}, "
            f"Value = {values[i]}, "
            f"Ratio = {values[i] / weights[i]:.2f}"
        )




print("=" * 60)
print("             0/1 KNAPSACK PROBLEM")
print("=" * 60)



n = int(input("\nEnter number of items: "))

weights = []
values = []

print("\nEnter weight and value of each item:")

for i in range(n):

    weight = int(input(f"Weight of Item {i + 1}: "))
    value = int(input(f"Value of Item {i + 1}: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("\nEnter knapsack capacity: "))




print("\n" + "=" * 60)
print("INPUT DATA")
print("=" * 60)

print(f"{'Item':<10}{'Weight':<10}{'Value':<10}{'Ratio':<10}")

for i in range(n):

    ratio = values[i] / weights[i]

    print(
        f"{i + 1:<10}"
        f"{weights[i]:<10}"
        f"{values[i]:<10}"
        f"{ratio:<10.2f}"
    )

print("\nKnapsack Capacity:", capacity)




profit_value, profit_weight, profit_selected = \
    greedy_by_profit(weights, values, capacity)

weight_value, weight_weight, weight_selected = \
    greedy_by_weight(weights, values, capacity)

ratio_value, ratio_weight, ratio_selected = \
    greedy_by_ratio(weights, values, capacity)




bottom_value, bottom_weight, bottom_selected, dp = \
    knapsack_bottom_up(weights, values, capacity)




top_value, top_weight, top_selected, memo = \
    knapsack_top_down(weights, values, capacity)



display_result(
    "GREEDY BY PROFIT",
    profit_value,
    profit_weight,
    profit_selected,
    weights,
    values
)

display_result(
    "GREEDY BY WEIGHT",
    weight_value,
    weight_weight,
    weight_selected,
    weights,
    values
)

display_result(
    "GREEDY BY VALUE/WEIGHT RATIO",
    ratio_value,
    ratio_weight,
    ratio_selected,
    weights,
    values
)

display_result(
    "BOTTOM-UP DYNAMIC PROGRAMMING",
    bottom_value,
    bottom_weight,
    bottom_selected,
    weights,
    values
)

display_result(
    "TOP-DOWN DYNAMIC PROGRAMMING",
    top_value,
    top_weight,
    top_selected,
    weights,
    values
)




print("\n" + "=" * 60)
print("FINAL COMPARISON")
print("=" * 60)

print(f"{'Method':<35}{'Value':<10}{'Weight':<10}")
print("-" * 60)

print(
    f"{'Greedy by Profit':<35}"
    f"{profit_value:<10}"
    f"{profit_weight:<10}"
)

print(
    f"{'Greedy by Weight':<35}"
    f"{weight_value:<10}"
    f"{weight_weight:<10}"
)

print(
    f"{'Greedy by Ratio':<35}"
    f"{ratio_value:<10}"
    f"{ratio_weight:<10}"
)

print(
    f"{'Bottom-Up DP':<35}"
    f"{bottom_value:<10}"
    f"{bottom_weight:<10}"
)

print(
    f"{'Top-Down DP':<35}"
    f"{top_value:<10}"
    f"{top_weight:<10}"
)



print("\n" + "=" * 60)
print("OPTIMAL SOLUTION")
print("=" * 60)

print("Maximum Value :", bottom_value)
print("Total Weight  :", bottom_weight)

print("Selected Items:", end=" ")

for i in bottom_selected:
    print(f"Item {i + 1}", end=" ")

print()



print("\n" + "=" * 60)
print("TIME COMPLEXITY")
print("=" * 60)

print("Greedy by Profit       : O(n log n)")
print("Greedy by Weight       : O(n log n)")
print("Greedy by Ratio        : O(n log n)")
print("Bottom-Up DP           : O(n × W)")
print("Top-Down DP            : O(n × W)")

print("\nSpace Complexity:")
print("Greedy approaches      : O(n)")
print("Bottom-Up DP           : O(n × W)")
print("Top-Down DP            : O(n × W)")

print("\nNote:")
print("For 0/1 Knapsack, Dynamic Programming gives")
print("the optimal solution, while greedy strategies")
print("do not always guarantee the optimal solution.")