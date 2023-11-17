import pytest
from avg_comparator import AverageComparator

def test_compare_averages_first_list_greater():
    comparator = AverageComparator([1, 2, 3], [4, 5, 6])
    result = comparator.compare_averages()
    assert result == "Первый список имеет большее среднее значение"

def test_compare_averages_second_list_greater():
    comparator = AverageComparator([4, 5, 6], [1, 2, 3])
    result = comparator.compare_averages()
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_lists_equal():
    comparator = AverageComparator([1, 2, 3], [4, 5, 6])
    result = comparator.compare_averages()
    assert result == "Средние значения равны"

def test_compare_averages_empty_lists():
    comparator = AverageComparator([], [])
    result = comparator.compare_averages()
    assert result == "Средние значения равны"

def test_compare_averages_first_list_empty():
    comparator = AverageComparator([], [4, 5, 6])
    result = comparator.compare_averages()
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_second_list_empty():
    comparator = AverageComparator([1, 2, 3], [])
    result = comparator.compare_averages()
    assert result == "Первый список имеет большее среднее значение"