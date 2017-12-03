from nose.tools import assert_equal
from parameterized import parameterized
from day_01 import InverseCaptia as ic

@parameterized([
    ("1122", "3"),
    ("1111", "4"),
    ("1234", "0"),
    ("91212129", "9")
])
def test_simple(cycle, result):
    assert_equal(ic.captia(cycle), result)

@parameterized([
    ("1212", "6"),
    ("1221", "0"),
    ("123425", "4"),
    ("123123", "12"),
    ("12131415", "4")
])
def test_advanced(cycle, result):
    assert_equal(ic.captia(cycle, len(cycle) / 2), result)
