#!/usr/bin/env python3

count = 0

def knapsack(capacity, weights, values, lookup_table=None):
    global count
    count += 1

    if lookup_table is None:
        lookup_table = {}

    n = len(weights)
    if n == 0 or capacity == 0:
        return 0

    if (n, capacity) in lookup_table:
        return lookup_table[(n, capacity)]

    if weights[-1] > capacity:
        result = knapsack(capacity, weights[:-1], values[:-1], lookup_table)
    else:
        result = max(
            knapsack(capacity, weights[:-1], values[:-1], lookup_table),
            values[-1] + knapsack(capacity - weights[-1], weights[:-1], values[:-1], lookup_table)
        )

    lookup_table[(n, capacity)] = result
    return result

if __name__ == "__main__":
    print("The maximum value in the knapsack is:", knapsack(50, [10, 20, 30], [60, 100, 120]))
    print("Number of function calls:", count)
