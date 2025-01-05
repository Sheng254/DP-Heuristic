import numpy as np

def classical_dp_qkp(weights, profits, capacity):
    """
    Classical DP for QKP with backtracking to retrieve the selected items.

    Parameters:
    - weights: List of item weights.
    - profits: Quadratic profit matrix.
    - capacity: Knapsack capacity.

    Returns:
    - selected_items: A set of selected item indices.
    - max_profit: The total profit achieved by the selected items.
    """
    n = len(weights)

    # DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    # Tracker for backtracking
    tracker = [[set() for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Populate the DP table
    for k in range(1, n + 1):
        for r in range(capacity + 1):
            # Case 1: Do not include item k-1
            dp[k][r] = dp[k - 1][r]
            tracker[k][r] = tracker[k - 1][r].copy()

            # Case 2: Include item k-1 if it fits
            if r >= weights[k - 1]:
                prev_r = r - weights[k - 1]

                # Calculate profit with item k-1 included
                profit_with_k = dp[k - 1][prev_r]  # Base profit from previous state

                # Add self-profit (can be zero, doesn't affect calculations)
                profit_with_k += profits[k - 1][k - 1]

                # Add interaction profits with previously selected items
                for j in tracker[k - 1][prev_r]:
                    profit_with_k += profits[k - 1][j]

                # Update DP table and tracker if this inclusion gives a higher profit
                if profit_with_k > dp[k][r]:
                    dp[k][r] = profit_with_k
                    tracker[k][r] = tracker[k - 1][prev_r].copy()
                    tracker[k][r].add(k - 1)

    # Retrieve the maximum profit and the corresponding items
    max_profit = max(dp[n])
    max_capacity = dp[n].index(max_profit)
    selected_items = tracker[n][max_capacity]

    return selected_items, float(max_profit)

def dp_heuristic_algo2(weights, profits, capacity):
    """
    Heuristic DP algorithm 2 that tracks selected items to account for quadratic profits.

    Parameters:
    - weights: List of item weights.
    - profits: Quadratic profit matrix.
    - capacity: Knapsack capacity.

    Returns:
    - selected_items: A set of selected item indices.
    - max_profit: The total profit achieved by the selected items.
    """
    n = len(weights)
    dp = np.full((n + 1, capacity + 1), -np.inf)
    selected_items = [[set() for _ in range(capacity + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for k in range(1, n + 1):
        for r in range(capacity + 1):
            # Not taking item k-1
            dp[k][r] = dp[k - 1][r]
            selected_items[k][r] = selected_items[k - 1][r].copy()

            # Taking item k-1
            if r >= weights[k - 1]:
                prev_r = r - weights[k - 1]
                prev_profit = dp[k - 1][prev_r]
                if prev_profit != -np.inf:
                    # Calculate new profit: p_i + sum of q_{i,j} for all j in selected_items[k-1][prev_r]
                    current_profit = prev_profit + profits[k - 1][k - 1]
                    for i in selected_items[k - 1][prev_r]:
                        current_profit += profits[k - 1][i]

                    # Update profit and items (with tie-breaking)
                    if current_profit > dp[k][r] or (
                        current_profit == dp[k][r] and len(selected_items[k - 1][prev_r]) + 1 > len(selected_items[k][r])
                    ):
                        dp[k][r] = current_profit
                        selected_items[k][r] = selected_items[k - 1][prev_r].copy()
                        selected_items[k][r].add(k - 1)

    # Find the maximum profit and corresponding weight
    best_r = np.argmax(dp[n])  # Optimized result extraction
    max_profit = dp[n][best_r]
    return selected_items[n][best_r], max_profit

def dp_heuristic_algo3(weights, profits, capacity):
    """
    DP heuristic algorithm 3 that approximates quadratic profits

    Parameters:
    - weights: List of item weights.
    - profits: Quadratic profit matrix.
    - capacity: Knapsack capacity.

    Returns:
    - selected_items: A set of selected item indices.
    - max_profit: The total profit achieved by the selected items.
    """
    n = len(weights)
    dp = np.full(capacity + 1, -np.inf)
    item_inclusion = [set() for _ in range(capacity + 1)]
    dp[0] = 0  # Base case: zero capacity, zero profit

    for k in range(n):
        for r in range(capacity, weights[k] - 1, -1):  # Backward update
            prev_r = r - weights[k]
            if dp[prev_r] != -np.inf:  # Ensure previous state is valid
                # Calculate new profit: p_k + sum of q_{k,j} for all j in item_inclusion[prev_r]
                current_profit = dp[prev_r] + profits[k][k]
                for j in item_inclusion[prev_r]:
                    current_profit += profits[k][j]

                # Update dp[r] and item inclusion with tie-breaking
                if current_profit > dp[r] or (
                    current_profit == dp[r] and len(item_inclusion[prev_r]) + 1 > len(item_inclusion[r])
                ):
                    dp[r] = current_profit
                    item_inclusion[r] = item_inclusion[prev_r].copy()
                    item_inclusion[r].add(k)

    max_profit = np.max(dp)
    best_r = np.argmax(dp)
    selected_items = item_inclusion[best_r]
    return selected_items, max_profit

def run_classical_dp(weights, profits, capacity):
    return classical_dp_qkp(weights, profits, capacity)

def run_heuristic_algo2(weights, profits, capacity):
    return dp_heuristic_algo2(weights, profits, capacity)

def run_heuristic_algo3(weights, profits, capacity):
    return dp_heuristic_algo3(weights, profits, capacity)
