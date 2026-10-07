def calculate_area_square(side):
    """
    Calculate the area of a square.

    Parameters:
        side (int or float): Length of one side of the square.

    Returns:
        int or float: Area of the square.

    Raises:
        TypeError: If side is not a number.
        ValueError: If side is negative.
    """

    if not isinstance(side, (int, float)):
        raise TypeError("side must be a number")

    if side < 0:
        raise ValueError("side cannot be negative")

    return side * side


def calculate_cost(side, cost_per_unit):
    """
    Calculate the total cost based on the area of a square.

    Parameters:
        side (int or float): Length of one side of the square.
        cost_per_unit (int or float): Cost per square unit.

    Returns:
        int or float: Total cost.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are negative.
    """

    if not isinstance(cost_per_unit, (int, float)):
        raise TypeError("cost_per_unit must be a number")

    if cost_per_unit < 0:
        raise ValueError("cost_per_unit cannot be negative")

    area = calculate_area_square(side)

    return area * cost_per_unit
