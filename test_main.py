import py_user
import check_file

def test_file():
    try:
        output = check_file.check_file('database.txt')
        assert output.__eq__(True)
    except FileNotFoundError:
        print("No such file exists")
    except AssertionError:
        print("assert false")