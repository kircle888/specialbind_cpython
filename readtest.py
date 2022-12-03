import ast

with open("test.py","r") as f:
    code = f.read()

ast_node = ast.parse(code,'msg.log',mode='exec')
print(ast.dump(ast_node))