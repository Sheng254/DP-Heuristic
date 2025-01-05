# Dynamic Programming Heuristics for Solving the Quadratic Knapsack Problem (QKP)


## Table of Contents

1. [Abstract](#abstract)
2. [Overview of Algorithms](#overview-of-algorithms) 
3. [Test Case Overview](#test-case-overview)
4. [Test Case Results](#test-case-results)
5. [Performance and Complexity Analysis](#performance-and-complexity-analysis)
6. [Reference to the Research Paper](#reference-to-the-research-paper)

<br>

## Abstract
This repository implements dynamic programming (DP) heuristics for solving the Quadratic Knapsack Problem (QKP). The QKP is a variant of the classical knapsack problem where the profit matrix includes not only the individual item profits but also quadratic interactions between selected items. The repository introduces three algorithms: the classical DP approach as a baseline, Algorithm 2, and Algorithm 3. Algorithms 2 and 3 are based on the dynamic programming heuristic proposed in a 2014 paper by Fomeni and Letchford, published in INFORMS Journal on Computing. The project includes test cases and complexity analysis to validate the effectiveness of the algorithms. Among the three, Algorithm 3 is the most efficient in terms of both time and space complexity.

<br>

## Overview of Algorithms

The following table summarises the three algorithms for solving QKP:

| **Algorithm**          | **Description**                                                                                                      | **Key Features**                                                                                                     | **Complexity**                       |
|------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| **Classical DP** | A classical dynamic programming approach for solving QKP with backtracking to retrieve the selected items.           | - Standard DP approach with a 2D table.<br>- Backtracking to track selected items.<br>- Suitable for small instances. | Time complexity: O(n * capacity) <br> Space complexity: O(n * capacity)  |
| **Algorithm 2**  | A heuristic DP algorithm that improves upon the classical DP by tracking quadratic profit interactions.              | - Uses a 2D DP table.<br>- Incorporates quadratic profit matrix interactions.<br>- Offers better performance on larger instances. | Time complexity: O(n * capacity) <br> Space complexity: O(n * capacity)  |
| **Algorithm 3**  | A more optimised DP heuristic that approximates quadratic profits with improved time and space efficiency.            | - Optimised with 1D DP table.<br>- Performs backward updates for efficiency.<br>- Best time and space complexity among the three. | Time complexity: O(n * capacity) <br> Space complexity: O(capacity)      |

<br>

## Test Case Overview

Each test case evaluates the performance and correctness of the algorithms based on correctness, execution time, and memory usage. It is structured as a dictionary with the following key elements:

- **weights**: A list of integers representing the weights of the items.
- **profits**: A 2D list (matrix) of integers that represents the profit matrix, which includes both individual item profits (diagonal) and quadratic interaction profits (off-diagonal terms).
- **capacity**: An integer representing the capacity of the knapsack.
- **expected_selected_items**: A set of integers specifying the items that should be selected according to the optimal solution for the given test case.
- **expected_profit**: The total profit that should result from selecting the optimal set of items.

### Example of Test Case Format

```python
{
    'weights': [3, 4, 5],
    'profits': [
        [10, 2, 3],  # Item 1's profit interactions
        [2, 5, 4],   # Item 2's profit interactions
        [3, 4, 7]    # Item 3's profit interactions
    ],
    'capacity': 7,
    'expected_selected_items': {0, 1},  # Items selected: 0 and 1
    'expected_profit': 17  # Total profit: 10 + 5 + 2 = 17
}
```

### Reading the Profit Matrix

- The **diagonal elements** (e.g., `profits[i][i]`) represent the **self-profit** of each item.
- The **off-diagonal elements** (e.g., `profits[i][j]` for `i ≠ j`) represent the **quadratic profit** between two items. These values model the interaction profit when both items are selected together.

<br>

## Test Case Results

### Profit
| **Test Case** | **Expected Profit** | **Classical DP** | **Algorithm 2** | **Algorithm 3** |
|---------------|---------------------|------------------|-----------------|-----------------|
| **1**         | 17                  | 17.0             | 17.0            | 17.0            |
| **2**         | 16                  | 16.0             | 16.0            | 16.0            |
| **3**         | 28                  | 28.0             | 28.0            | 28.0            |
| **4**         | 18                  | 18.0             | 18.0            | 18.0            |
| **5**         | 31                  | 31.0             | 31.0            | 31.0            |
| **6**         | 56                  | 56.0             | 56.0            | 56.0            |
| **7**         | 58                  | 58.0             | 58.0            | 58.0            |
| **8**         | 0                   | 0.0              | 0.0             | 0.0             |
| **9**         | 88                  | 88.0             | 88.0            | 88.0            |
| **10**        | 50                  | 50.0             | 50.0            | 50.0            |

### Time Taken (in seconds)
| **Test Case** | **Classical DP** | **Algorithm 2** | **Algorithm 3** |
|---------------|------------------|-----------------|-----------------|
| **1**         | 0.000065 s       | 0.000122 s      | 0.000044 s      |
| **2**         | 0.000060 s       | 0.000105 s      | 0.000044 s      |
| **3**         | 0.000108 s       | 0.000209 s      | 0.000076 s      |
| **4**         | 0.000069 s       | 0.000126 s      | 0.000052 s      |
| **5**         | 0.000115 s       | 0.000210 s      | 0.000083 s      |
| **6**         | 0.000089 s       | 0.000170 s      | 0.000072 s      |
| **7**         | 0.000112 s       | 0.000266 s      | 0.000245 s      |
| **8**         | 0.000055 s       | 0.000058 s      | 0.000024 s      |
| **9**         | 0.000071 s       | 0.000135 s      | 0.000067 s      |
| **10**        | 0.000125 s       | 0.000279 s      | 0.000091 s      |

### Memory Usage (in MB)
| **Test Case** | **Classical DP** | **Algorithm 2** | **Algorithm 3** |
|---------------|------------------|-----------------|-----------------|
| **1**         | 0.007922 MB      | 0.008219 MB     | 0.002904 MB     |
| **2**         | 0.007016 MB      | 0.007298 MB     | 0.002680 MB     |
| **3**         | 0.013480 MB      | 0.013736 MB     | 0.003640 MB     |
| **4**         | 0.007560 MB      | 0.007816 MB     | 0.002456 MB     |
| **5**         | 0.012360 MB      | 0.012616 MB     | 0.003416 MB     |
| **6**         | 0.009800 MB      | 0.010056 MB     | 0.002904 MB     |
| **7**         | 0.013480 MB      | 0.013736 MB     | 0.003640 MB     |
| **8**         | 0.004040 MB      | 0.004248 MB     | 0.001728 MB     |
| **9**         | 0.006120 MB      | 0.006344 MB     | 0.001976 MB     |
| **10**        | 0.013566 MB      | 0.013768 MB     | 0.002904 MB     |

<br>

### Performance and Complexity Analysis
All 3 algorithms achieved correctness as they produced the same profit and selected items indices, which aligned with the expected ones.

In general, **Algorithm 3** is the most efficient as it requires the least time and memory across most test cases. Its optimised approach minimises resource usage, which leads to faster execution and lower memory consumption.

**Algorithm 2** is the least efficient, being the most resource-intensive. It consistently took the longest to execute and used the most memory, likely due to less efficient handling of data or suboptimal algorithmic design.

**Classical DP** performed better than **Algorithm 2**, using fewer resources, but still fell short compared to **Algorithm 3**. This is due to its relatively higher complexity.

<br>

## Reference to the Research Paper
The implementation of Algorithms 2 and 3 is based on the work presented in the following paper:
**Franklin Djeumou Fomeni, Adam N. Letchford (2014).** *A Dynamic Programming Heuristic for the Quadratic Knapsack Problem.* INFORMS Journal on Computing, 26(1):173-182. [https://doi.org/10.1287/ijoc.2013.0555](https://doi.org/10.1287/ijoc.2013.0555)