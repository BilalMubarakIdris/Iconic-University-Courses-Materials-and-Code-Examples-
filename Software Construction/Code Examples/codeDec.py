def calculate_statistics(numbers):
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        numbers (list): List of numeric values
        
    Returns:
        dict: Dictionary containing:
            - count: Number of elements
            - sum: Total of all numbers
            - mean: Average value
            - min: Minimum value
            - max: Maximum value
            
    Raises:
        ValueError: If input is empty or contains non-numeric values
        
    Example:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'count': 5, 'sum': 15, 'mean': 3.0, 'min': 1, 'max': 5}
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    try:
        return {
            "count": len(numbers),
            "sum": sum(numbers),
            "mean": sum(numbers) / len(numbers),
            "min": min(numbers),
            "max": max(numbers)
        }
    except TypeError:
        raise ValueError("All elements must be numeric")
