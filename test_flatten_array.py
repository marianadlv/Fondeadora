import pytest
from flatten_array import flatten_array


class TestFlattenArray:

    @pytest.mark.parametrize("test_input, expected_output",
                             [([1, [2, [3, [4, 5]]]], [1, 2, 3, 4, 5]),
                              ([1, [2]], [1, 2]),
                              ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
                              ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
                              ([[1], [2]], [1, 2]),
                              ([1, [2, 3, 4, 5]], [1, 2, 3, 4, 5]),
                              ([[1], 2], [1, 2]),
                              ([], [])])
    def test_correct_input(self, test_input, expected_output):
        output_array = flatten_array(test_input)
        assert output_array == expected_output

    @pytest.mark.parametrize("test_input", [[1.5, 2], [1, [2, [3, [4, 5.4]]]], [1, ["", [3, [4, 5]]]], 1])
    def test_incorrect_input(self, test_input):
        with pytest.raises(TypeError):
            flatten_array(test_input)
