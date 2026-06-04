from main import sum_delimiter_collection

def test_when_111_give_3():
    assert sum_delimiter_collection("1,1,1") == 3

def test_when_123_give_3():
    assert sum_delimiter_collection("1,2,3") == 6

def test_when_1tal2_give_0():
    assert sum_delimiter_collection("1,tal,2") == 0

def test_when_hello_give_0():
    assert sum_delimiter_collection("hola") == 0

def test_when_number_give_number():
    assert sum_delimiter_collection(12) == 12

def test_when_number_array_give_minus1():
    assert sum_delimiter_collection([1, 2, 3]) == -1

def test_when_string_array_give_minus1():
    assert sum_delimiter_collection(["hola", "2", "tal"]) == -1

