from expreval.parser import Parser
from expreval.evaluator import Evaluator

def test_parser_pass():
    assert Parser().parse('1+2')=='1+2'

def test_pow_eval_correct_1():
    assert Evaluator().eval(Parser().parse('2*3^2')) == 18

def test_pow_eval_correct_2():
    assert Evaluator().eval(Parser().parse('4*2^2')) == 16

def test_parser_produces_structured_output():
    result = Parser().parse('1+2')
    assert not isinstance(result, str)
