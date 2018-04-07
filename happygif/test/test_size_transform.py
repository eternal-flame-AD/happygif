import os
import sys


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


def test_size_tranform():
    from happygif import _pos_trans
    size = (100, 1000)
    result = _pos_trans('30%', '500', size)
    assert result == (30, 500)
    result = _pos_trans('30', '30%', size)
    assert result == (30, 300)