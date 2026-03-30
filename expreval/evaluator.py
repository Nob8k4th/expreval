import math
class Evaluator:
    def eval(self, ast, vars=None):
        vars = vars or {}
        expr = ast.replace('^','**')
        if expr.startswith('-('):
            return eval(expr[2:-1], {'__builtins__':{}}, vars)
        env={'sin':math.sin,'cos':math.cos,'sqrt':math.sqrt,'abs':abs,'floor':math.floor}
        env.update(vars)
        return eval(expr, {'__builtins__':{}}, env)
