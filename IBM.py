def findMaximumAlloys(composition, stock, cost, budget):
    n = len(composition)
    max_alloys = 0

    for units in range(1, budget + 1):
        extra_requirements = [max(0, units * composition[i] - stock[i]) for i in range(n)]
        total_cost = sum(extra_requirements[i] * cost[i] for i in range(n))

        if total_cost <= budget:
            max_alloys = units
        else:
            break

    return max_alloys

# Example usage
composition = [1, 2]
stock = [0, 1]
cost = [1, 1]
budget = 3

result = findMaximumAlloys(composition, stock, cost, budget)
print("Maximum units of alloys the company can produce:", result)
