from area import calculate_area_square, calculate_cost


def test_area_cost_integration():
    result = calculate_cost(4, 10)
    assert result == 160
