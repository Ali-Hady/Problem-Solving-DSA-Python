from typing import List

def squared_area(binary_grid: List[List[int]]) -> int:
    """Calculate the area of the largest square submatrix containing only 1s.

    Args:
        binary_grid (List[List[int]]): A 2D binary grid.

    Returns:
        int: The area of the largest square submatrix containing only 1s.
        
    Time Complexity: O(n * m), where n is the number of rows and m is the number of columns in the grid.
    Space Complexity: O(n * m), where n is the number of rows and m is the number of columns in the grid.
    """
    n = len(binary_grid)
    m = len(binary_grid[0])
    
    dp = [[0] * m for _ in range(n)]
    max_side = 0
    for i in range(n):
        for j in range(m):
            if binary_grid[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                max_side = max(max_side, dp[i][j])
                
    return max_side * max_side


def squared_area_optimized(binary_grid: List[List[int]]) -> int:
    """Calculate the area of the largest square submatrix containing only 1s.

    Args:
        binary_grid (List[List[int]]): A 2D binary grid.

    Returns:
        int: The area of the largest square submatrix containing only 1s.
        
    Time Complexity: O(n * m), where n is the number of rows and m is the number of columns in the grid.
    Space Complexity: O(m), where m is the number of columns in the grid.
    """
    n = len(binary_grid)
    m = len(binary_grid[0])
    
    dp = [0] * m
    max_side = 0
    prev = 0 # to store the value of dp[i-1][j-1]
    
    for i in range(n):
        for j in range(m):
            temp = dp[j] # store current dp[j] value before updating -> to use it for prev
            if binary_grid[i][j] == 1:
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], dp[j-1], prev) + 1 # we update the new dp[j] value (in place)
                    # dp[j] corresponds to dp[i-1][j], dp[j-1] corresponds to dp[i][j-1], and prev corresponds to dp[i-1][j-1]
                    
                max_side = max(max_side, dp[j])
                
            else:
                dp[j] = 0
                    
            prev = temp

    return max_side * max_side


# Example usage
if __name__ == "__main__":
    binary_grid = [
        [1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1]
    ]
    print(squared_area(binary_grid))  # Output: 9
    print(squared_area_optimized(binary_grid))  # Output: 9