# a file that parses itself and dumps the size of its own ast

import ast

class visitor(ast.NodeVisitor):
  def __init__(self):
    self.nodes = []
  def generic_visit(self, node):
    self.nodes.append(type(node).__name__)
    ast.NodeVisitor.generic_visit(self, node)

if __name__ == '__main__':
  code = open(__file__).read()
  t = ast.parse(code)
  print ast.dump(t)
  v = visitor()
  v.visit(t)
  print len(v.nodes)
