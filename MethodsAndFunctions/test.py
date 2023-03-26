from main import is_even, is_even_list


def test_is_even():
    assert (is_even([1, 1, 1, 5, 2])) == True


def test_is_odd():
    assert (is_even([5, 3, 7])) == False


def test_is_even_list():
    numbers = [1, 2, 3, 4, 5, 6]
    even = [2, 4, 6]
    assert is_even_list(numbers) == even

