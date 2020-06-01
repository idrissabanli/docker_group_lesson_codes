from scripts.math_lib import sum, divide
import pytest

@pytest.mark.parametrize("given_value1, given_value2, expected_result", [(1,4,5), (10000, 100000,110000), (11, 10,21), (-2, -4,-6)])
def test_sum(given_value1, given_value2, expected_result):
    actual_result = sum(given_value1, given_value2)
    assert expected_result == actual_result


@pytest.mark.parametrize("given_value1, given_value2, expected_result", [(4,2,2.0), (8,2,4.0), (8,0,'You can not divide by zero')])
def test_divide(given_value1, given_value2, expected_result):
    actual_result = divide(given_value1, given_value2)
    assert expected_result == actual_result

