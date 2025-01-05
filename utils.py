from itertools import combinations
import time
import tracemalloc

def compute_profit_and_items(weights, profits, capacity, selected_indices):
    """
    Helper function to compute the total profit and validate the selected items 
    for a given set of indices in the Quadratic Knapsack Problem.

    Parameters:
    - weights: List of item weights.
    - profits: Quadratic profit matrix.
    - capacity: Knapsack capacity.
    - selected_indices: Set of indices of selected items.

    Returns:
    - (total_profit, valid_selected_items): Tuple containing:
        * total_profit: The computed profit for the selected items (or None if overweight).
        * valid_selected_items: The subset of selected items that fit within the capacity.
    """
    total_weight = sum(weights[i] for i in selected_indices)
    
    # Check if the total weight exceeds capacity
    if total_weight > capacity:
        return None, set()
    
    total_profit = 0
    valid_selected_items = set(selected_indices)
    
    # Add linear profits
    for i in valid_selected_items:
        total_profit += profits[i][i]
    
    # Add quadratic profits
    for i, j in combinations(valid_selected_items, 2):
        total_profit += profits[i][j]
    
    return total_profit, valid_selected_items

def measure_complexity(algorithms, weights, profits, capacity, runs=5):
    """
    Measures the time and space complexity of given algorithms over multiple runs.

    Parameters:
    - algorithms: A dictionary of algorithm names and their corresponding functions.
    - weights: List of item weights.
    - profits: Quadratic profit matrix.
    - capacity: Knapsack capacity.
    - runs: Number of runs to average the results.

    Returns:
    - A dictionary containing average time and memory usage for each algorithm.
    """
    results = {}

    for name, algo in algorithms.items():
        times = []
        memories = []

        for _ in range(runs):
            # Start tracking memory
            tracemalloc.start()

            # Measure execution time
            start_time = time.perf_counter()
            algo(weights, profits, capacity)
            end_time = time.perf_counter()

            # Stop tracking memory
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Record results for this run
            times.append(end_time - start_time)
            memories.append(peak / 10**6)  # Convert to MB

        # Average results across runs
        avg_time = sum(times) / runs
        avg_memory = sum(memories) / runs

        # Correctly populate the results dictionary
        results[name] = {
            "Avg Time (seconds)": avg_time,
            "Avg Memory (MB)": avg_memory,
            "Runs": runs
        }

    return results
