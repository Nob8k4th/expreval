import math
from expreval.evaluator import Evaluator

def test_basic_pass():
    assert Evaluator().eval('1+2')==3

def test_vars_pass():
    assert Evaluator().eval('x+1', {'x':2})==3

def test_func_pass():
    assert round(Evaluator().eval('sin(0)'),5)==0.0

def test_sqrt_pass():
    assert Evaluator().eval('sqrt(4)')==2

def test_floor_pass():
    assert Evaluator().eval('floor(3.7)')==3

def test_unary_fail1():
    assert Evaluator().eval('-(2+3)')==-5

def test_unary_fail2():
    assert Evaluator().eval('-(1+1)')==-2

def test_unary_fail3():
    assert Evaluator().eval('-(3*2)')==-6
