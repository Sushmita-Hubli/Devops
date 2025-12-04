#app.py
#code for addition functionality 
def add(a, b):
    return a+b

#code for testing
def test_add():
    assert add(1,2) == 3
    assert add(1,-1) == 0
