def calculate_area_square(length: int | float) -> int | float:  
    """  
    Function to calculate the area of a square  
    :param length: length of the square  
    :return: area of the square  
    """  
    if not isinstance(length, (int, float)) or length <= 0:  
        raise TypeError("Length must be a positive non-zero number")  
    return length * length

def calculate_cost(side, cost_per_unit):
    area = calculate_area_square(side)
    return area * cost_per_unit
