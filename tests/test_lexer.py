import pytest
from expreval.lexer import Lexer, LexError

def test_float_pass():
    assert '3.14' in Lexer().tokenize('3.14 + 1')

def test_tokens_pass():
    assert Lexer().tokenize('(1+2)')[0]=='('

def test_ge_fail_should_lexerror():
    with pytest.raises(LexError):
        Lexer().tokenize('a >= b')

def test_var_pass():
    assert 'x' in Lexer().tokenize('x + 1')

def test_tokenize_operators_pass():
    tokens = Lexer().tokenize('3 + 4 * 2')
    assert tokens == ['3', '+', '4', '*', '2']
