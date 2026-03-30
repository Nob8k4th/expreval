# expreval

`expreval` 是一个表达式求值工具链，包含分词、解析和执行三个步骤。

## 模块说明

- `Lexer`：将表达式字符串切分为 token 列表
- `Parser`：把表达式输入转成可执行结构
- `Evaluator`：支持变量与常见数学函数的求值

## 快速使用

```bash
pip install -e .
```

```python
from expreval import Lexer, Parser, Evaluator

expr = "sqrt(16) + x * 2"
tokens = Lexer().tokenize(expr)
ast = Parser().parse(expr)
value = Evaluator().eval(ast, {"x": 3})

print(tokens)
print(value)
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
