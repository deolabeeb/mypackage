from mypackage import myModule

def test_top_n():
    """
    Make sure top_n works correctly
    """
    
    assert myModule.top_n([8, 3, 3, 7, 4], 3) == [8, 7, 4], "Incorrect"
    assert myModule.top_n([10, 1, 12, 9, 2], 2) == [12, 10], "Incorrect"
    assert myModule.top_n([1, 2, 3, 4, 5], 5) == [6, 4, 3, 2, 1], "Incorrect"