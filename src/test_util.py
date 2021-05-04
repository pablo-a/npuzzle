import util
import pytest


def test_flatten_nested_list():
    t1 = [[1, 2, 3], [4, 5, 6]]
    t2 = [1, 2, [3, 4], [5, [6]]]
    assert util.flatten_nested_list(t1) == [1, 2, 3, 4, 5, 6]
    with pytest.raises(TypeError):
        util.flatten_nested_list(t2) == [1, 2, 3, 4, 5, [6]]
