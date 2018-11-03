import unittest
from ast import get_ast
from tree import TreeNode, SimpleTree

def get_tree_ast(str):
    """Возвращает AST
    """
    lst = get_ast(str)
    tree_ast = SimpleTree(TreeNode(None, None))
    new_lst = lst.copy()
    while len(new_lst) != 0:
        token = new_lst.pop(0)
        if token == '(':
            tree_ast.add_child(TreeNode(tree_ast.current, None))
            tree_ast.current = tree_ast.current.child[0]
        elif token == ')':
            tree_ast.current = tree_ast.current.parent
        elif token != '/' and token != '*' and token != '-' and token != '+':
            tree_ast.current.value = token
            tree_ast.current = tree_ast.current.parent
        else:
            tree_ast.current.value = token
            tree_ast.add_child(TreeNode(tree_ast.current, None))
            tree_ast.current = tree_ast.current.child[1]
    return tree_ast  


class TestGetTreeAst(unittest.TestCase):
    """Проверка визуального представления AST 
    """
    def test_get_tree_ast(self):
        self.str = '(3+(5-7))'
        self.ls = get_tree_ast(self.str)
        self.assertEqual(self.ls.count_nodes(), ['+', '3', '-', '5', '7'])  
        self.str = '((7+3)*(5-2))'
        self.lst = get_tree_ast(self.str)
        self.assertEqual(self.lst.count_nodes(), ['*', '+', '7', '3', '-', '5', '2'])
        
if __name__ == '__main__':
    unittest.main()  
   