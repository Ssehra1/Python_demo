def calculate_area_square(side):
    return side * side


def calculate_cost(side, cost_per_unit):
    area = calculate_area_square(side)
    return area * cost_per_unit
