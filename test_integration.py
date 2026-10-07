from area import calculate_area_square, calculate_cost


def test_area_cost_integration():
    area = calculate_area_square(4)
    cost = calculate_cost(4, 10)

    assert area == 16
    assert cost == 160
