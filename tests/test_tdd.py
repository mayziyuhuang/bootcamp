# py.test gives the testing functionality
import pytest
import lesson35
# We'll use our bioinformatics dictionary from before
import bioinfo_dicts as bd

def test_n_neg():
    assert lesson35.n_neg('E') == 1
    assert lesson35.n_neg('D') == 1
    assert lesson35.n_neg('') == 0
    assert lesson35.n_neg('ACKLWTTAE') == 1
    assert lesson35.n_neg('DDDDEEEE') == 8
    assert lesson35.n_neg('acklwttae') == 1

    pytest.raises(RuntimeError, "lesson35.n_neg('Z')")

# make a tests file under git/bootcamp
# if the file name has test_
# in terminal, you can use py.test to test all the files in tests and with test_
# add a new file in termianl: mkdir tests
# move a file into tests file: mv test_tdd.py tests/
