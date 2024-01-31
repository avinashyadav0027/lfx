import pytest
import hypothesis.strategies as st
from hypothesis import given
from process_list import process_integer_list

@given(st.lists(st.integers(), min_size=0, max_size=3).flatmap(lambda lst: st.lists(st.integers(), min_size=len(lst) * 10, max_size=len(lst) * 10)))
def test_valid_input(input_list):
    """
    Test the process_integer_list function with valid input.

    Args:
        input_list (list): A list of integers with a length of 10.

    Raises:
        AssertionError: If the processed list does not meet the specified criteria.
        Criteria :- Elements at positions that are multiples of 2 or 3 are removed.
    """
    processed_list = process_integer_list(input_list)

    # Check that elements at positions that are multiples of 2 or 3 are removed
    j = 0
    for i, elem in enumerate(input_list):
        if (i + 1) % 2 == 0 or (i + 1) % 3 == 0:
            continue
        assert elem == processed_list[j]
        j += 1
        
@given(st.lists(st.integers(), min_size=1, max_size=30).filter(lambda x: len(x) % 10 != 0))
def test_invalid_length(input_list):
    """
    Test the process_integer_list function with an invalid input length.

    Raises:
        pytest.raises: If the input length is not a multiple of 10.
    """
    with pytest.raises(ValueError, match="The length of the list must be a multiple of 10."):
        process_integer_list(input_list)
