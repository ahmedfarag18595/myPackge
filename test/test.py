from mypackage import myModule

def test_top_n():
    assert myModule.top_n([8,5,2,3,6],3) == [8,6,5], "incorrect"
    assert myModule.top_n([80,50,20,30,60],3) == [80,60,50], "incorrect"
    assert myModule.top_n([18,15,12,13,16],3) == [18,16,15], "incorrect"