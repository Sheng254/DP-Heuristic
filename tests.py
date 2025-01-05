from algorithms import classical_dp_qkp, dp_heuristic_algo2, dp_heuristic_algo3
from utils import compute_profit_and_items, measure_complexity
from algorithms import run_classical_dp, run_heuristic_algo2, run_heuristic_algo3

def test_qkp_algorithms():
    """
    Tests various algorithms for the Quadratic Knapsack Problem using predefined test cases.

    Each test case specifies the weights, profits, capacity, and the expected result 
    (selected items and total profit). Validates the correctness of the algorithms by 
    comparing their outputs to the expected values.

    Also validates the expected results using the helper function 
    `compute_profit_and_items`.

    ### Profit Matrix Interpretation:
    The profit matrix captures both the individual values of items (linear profits) 
    and the pairwise interactions (quadratic profits).

    Example:
    profits = [
        [5, 2, 4, 1],  # Row 0: Profits related to Item 1
        [2, 6, 3, 2],  # Row 1: Profits related to Item 2
        [4, 3, 8, 5],  # Row 2: Profits related to Item 3
        [1, 2, 5, 7]   # Row 3: Profits related to Item 4
    ]

    - Item 1 (Row 0):
      - Self-profit: `profits[0][0] = 5`
      - Interaction with Item 2: `profits[0][1] = 2`
      - Interaction with Item 3: `profits[0][2] = 4`
      - Interaction with Item 4: `profits[0][3] = 1`
    - Item 2 (Row 1):
      - Self-profit: `profits[1][1] = 6`
      - Interaction with Item 1: `profits[1][0] = 2`
      - Interaction with Item 3: `profits[1][2] = 3`
      - Interaction with Item 4: `profits[1][3] = 2`

    Outputs:
    - The correctness of each algorithm for each test case.
    - A complexity analysis for each algorithm (average time and memory usage).

    Parameters:
    - None

    Returns:
    - None
    """
    test_cases = [
        # Format: (weights, profits, capacity, expected_selected_items, expected_profit)

        # Test Case 1: Basic small problem
        {
            'weights': [3, 4, 5],
            'profits': [
                [10, 2, 3],
                [2, 5, 4],
                [3, 4, 7]
            ],
            'capacity': 7,
            'expected_selected_items': {0, 1},  # Items 0 and 1
            'expected_profit': 10 + 5 + 2  # Total = 17
        },

        # Test Case 2: Symmetric profits with moderate capacity
        {
            'weights': [2, 3, 4],
            'profits': [
                [5, 3, 1],
                [3, 8, 4],
                [1, 4, 6]
            ],
            'capacity': 6,
            'expected_selected_items': {0, 1},  # Optimal selection within capacity
            'expected_profit': 5 + 8 + 3  # Total = 16
        },

        # Test Case 3: Larger problem with diverse weights
        {
            'weights': [2, 3, 4, 5],
            'profits': [
                [6, 2, 4, 1],
                [2, 5, 3, 2],
                [4, 3, 8, 5],
                [1, 2, 5, 9]
            ],
            'capacity': 10,
            'expected_selected_items': {0, 1, 2},  # Items 0, 1, 2
            'expected_profit': 6 + 5 + 8 + 2 + 4 + 3 # Total = 28
        },

        # Test Case 4: Sparse profits, only diagonal terms matter
        {
            'weights': [1, 3, 4, 2],
            'profits': [
                [7, 0, 0, 0],
                [0, 8, 0, 0],
                [0, 0, 9, 0],
                [0, 0, 0, 10]
            ],
            'capacity': 5,
            'expected_selected_items': {1, 3},  # Items 1 and 3
            'expected_profit': 8 + 10  # Total = 18
        },

        # Test Case 5: Dense quadratic terms
        {
            'weights': [3, 2, 4, 3],
            'profits': [
                [5, 2, 4, 1],
                [2, 6, 3, 2],
                [4, 3, 8, 5],
                [1, 2, 5, 7]
            ],
            'capacity': 9,
            'expected_selected_items': {1, 2, 3},  # Items 1, 2, 3
            'expected_profit': 6 + 8 + 7 + 3 + 2 + 5  # Total = 31
        },

        # Test Case 6: High self-profits with weak interactions
        {
            'weights': [2, 3, 4, 1],
            'profits': [
                [15, 1, 2, 1],
                [1, 20, 2, 1],
                [2, 2, 25, 3],
                [1, 1, 3, 10]
            ],
            'capacity': 7,
            'expected_selected_items': {0, 2, 3},  # Items 0, 2, 3
            'expected_profit': 15 + 25 + 10 + 2 + 1 + 3  # Total = 56
        },

        # Test Case 7: Complex asymmetric profits
        {
            'weights': [3, 4, 2, 5],
            'profits': [
                [10, 5, 3, 7],
                [5, 15, 8, 2],
                [3, 8, 12, 6],
                [7, 2, 6, 20]
            ],
            'capacity': 10,
            'expected_selected_items': {0, 2, 3},  # Items 0, 2, 3
            'expected_profit': 10 + 12 + 20 + 3 + 7 + 6  # Total = 58
        },

        # Test Case 8: Edge case - Capacity too small to hold any item
        {
            'weights': [5, 4, 6, 7],
            'profits': [
                [10, 2, 3, 4],
                [2, 5, 4, 6],
                [3, 4, 7, 1],
                [4, 6, 1, 9]
            ],
            'capacity': 2,
            'expected_selected_items': set(),  # No items can be selected
            'expected_profit': 0
        },

        # Test Case 9: Edge case - All weights 1 (favoring dense packing)
        {
            'weights': [1, 1, 1, 1, 1],
            'profits': [
                [1, 2, 3, 4, 5],
                [2, 6, 7, 8, 9],
                [3, 7, 12, 13, 14],
                [4, 8, 13, 15, 16],
                [5, 9, 14, 16, 18]
            ],
            'capacity': 3,
            'expected_selected_items': {2, 3, 4},  # Items 2, 3, 4
            'expected_profit': 12 + 15 + 18 + 13 + 14 + 16  # Total = 88
        },

        # Test Case 10: Large and sparse problem
        {
            'weights': [1, 3, 2, 4, 6, 5],
            'profits': [
                [10, 5, 0, 0, 0, 0],  
                [5, 15, 8, 0, 0, 0], 
                [0, 8, 12, 6, 0, 0],  
                [0, 0, 6, 20, 5, 0],  
                [0, 0, 0, 5, 30, 10],
                [0, 0, 0, 0, 10, 25] 
            ],
            'capacity': 7,  # Strict capacity ensures competing subsets cannot fit
            'expected_selected_items': {0, 1, 2},  # Items 0, 1, 2
            'expected_profit': 10 + 15 + 12 + 5 + 8  # Total = 50
        }
    ]

    for idx, test in enumerate(test_cases, 1):
        weights = test['weights']
        profits = test['profits']
        capacity = test['capacity']
        expected_items = test['expected_selected_items']
        expected_profit = test['expected_profit']

        # Validate expected values using compute_profit_and_items
        computed_profit, computed_items = compute_profit_and_items(weights, profits, capacity, expected_items)
        expected_correct = computed_profit == expected_profit and computed_items == expected_items

        # Run algorithms
        classical_items, classical_profit = classical_dp_qkp(weights, profits, capacity)
        heuristic2_items, heuristic2_profit = dp_heuristic_algo2(weights, profits, capacity)
        heuristic3_items, heuristic3_profit = dp_heuristic_algo3(weights, profits, capacity)

        # Check correctness of algorithms
        classical_correct = classical_profit == expected_profit and classical_items == expected_items
        heuristic2_correct = heuristic2_profit == expected_profit
        heuristic3_correct = heuristic3_profit == expected_profit

        # Output results and check correctness
        print(f"Test Case {idx}:")
        if expected_correct:
            # If expected matches computed, show only expected values
            print(f"  Expected Profit        : {expected_profit}")
            print(f"  Expected Selected Items: {expected_items}")
        else:
            # If mismatch, show both expected and computed values
            print(f"  Expected Profit        : {expected_profit}, Computed Profit = {computed_profit}, Correct: {'✅' if expected_correct else '❌'}")
            print(f"  Expected Selected Items: {expected_items}, Computed Items = {computed_items}, Correct: {'✅' if expected_correct else '❌'}")

        print("\n  Algorithm Results:")
        print(f"  • Classical DP       : Profit = {classical_profit}, Items = {classical_items}, Correct: {'✅' if classical_correct else '❌'}")
        print(f"  • DP Heuristic Algo 2: Profit = {heuristic2_profit}, Items = {heuristic2_items}, Correct: {'✅' if heuristic2_correct else '❌'}")
        print(f"  • DP Heuristic Algo 3: Profit = {heuristic3_profit}, Items = {heuristic3_items}, Correct: {'✅' if heuristic3_correct else '❌'}")

        # Define algorithms dictionary for this test case
        algorithms = {
            "Classical DP": classical_dp_qkp,
            "Heuristic Algo 2": dp_heuristic_algo2,
            "Heuristic Algo 3": dp_heuristic_algo3
        }

        # Measure complexity for each algorithm
        complexity = measure_complexity(algorithms, weights, profits, capacity)
        print("\n  Complexity Analysis:")
        for algo_name, stats in complexity.items():
            print(f"  • {algo_name:19}: Time = {stats['Avg Time (seconds)']:.6f} seconds, Memory = {stats['Avg Memory (MB)']:.6f} MB")

        print("-" * 70)

if __name__ == "__main__":
    test_qkp_algorithms()
    