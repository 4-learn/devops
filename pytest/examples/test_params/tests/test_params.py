import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import check_machine 

def test_params():
    a = 1
    b = 1 
    assert check_machine(a, b) == True
