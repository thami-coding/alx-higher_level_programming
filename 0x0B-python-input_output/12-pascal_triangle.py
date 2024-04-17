"""
Module: pascal_triangle_generator

This module contains a function for generating Pascal's triangle up to a specified number of rows.
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Parameters:
    - n (int): The number of rows in Pascal's triangle.

    Returns:
    - List[List[int]]: A list of lists of integers representing Pascal's triangle.
      Returns an empty list if n <= 0.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []
    
    # Initialize Pascal's triangle with the first row
    triangle = [[1]]
    
    # Generate subsequent rows
    for i in range(1, n):
        # Create a new row
        row = [1]
        
        # Fill the row according to Pascal's triangle rule
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        row.append(1)
        
        # Append the new row to the triangle
        triangle.append(row)
    
    return triangle
