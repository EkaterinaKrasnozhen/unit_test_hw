import pytest

from Average import Average
from Average_list import Average_of_two_list


@pytest.fixture
def setup():
    average = Average
    average_2list = Average_of_two_list
    return average, average_2list

# @pytest.mark.parametrize('lst1, result', [
#     ([1, 2, 3, 4, 5], 3),
#     ([4, 4], 4),
#     ([1, 1, 1, 5], 2),
#     ([0, 1], 0.5)
# ])
# def test_avg(lst1, result):
#     average = Average()
#     assert average.average(lst1) == result, 'test multiply failed'


def test_average(setup):
    average, _ = setup
    lst = [1, 2, 3, 4, 5]
    assert average.average(lst) == 3.0, 'test_average failed'


def test_empty_average(setup):
    average, _ = setup
    assert average.average([]) == 0.0, 'test empty_average failed'


def test_average_one_num(setup):
    average, _ = setup
    lst = [1]
    assert average.average(lst) == 1.0, 'test with one num failed'


def test_average_two_list_gt(setup):
    _, average_2list = setup
    lst1 = [2, 2, 2]
    lst2 = [3, 3, 3]
    assert average_2list.average_two_lst(
        lst1, lst2) == 'Второй список имеет большее среднее значение', 'test_average_two_list_gt failed'


def test_average_two_list_lt(setup):
    _, average_2list = setup
    lst2 = [2, 2, 2]
    lst1 = [3, 3, 3]
    assert average_2list.average_two_lst(
        lst1, lst2) == 'Первый список имеет большее среднее значение', 'test_average_two_list_lt failed'


def test_average_two_list_same(setup):
    _, average_2list = setup
    lst1 = [2, 2, 2]
    lst2 = [2, 2, 2]
    assert average_2list.average_two_lst(
        lst1, lst2) == 'Средние значения равны', 'test_average_two_list_same failed'


def test_average_two_list_not_list(setup):
    _, average_2list = setup
    with pytest.raises(TypeError):
        average_2list.average_two_lst(1, 2)


if __name__ == '__main__':
    pytest.main(['-v'])
