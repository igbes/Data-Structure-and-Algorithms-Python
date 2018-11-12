import unittest

def get_ast(math_str):
    
    """Возвращает список токенов AST
    """
    
    def get_list(str):
        f = 0
        arr = []
        for i, elem in enumerate(str):
            if f == 1 and elem != '+' and elem != '-' and elem != '*'and elem != '/' and elem != ')' and elem != '(':
                arr[-1] += elem
                continue
            arr.append(elem)
            if elem != '+' and elem != '-' and elem != '*'and elem != '/' and elem != ')' and elem != '(':
                f = 1
            else:
                f = 0
        return arr

    def merge_parentheses(arr):
        new_arr = []
        f = 0
        for i, elem in enumerate(arr):
            if f == 0:
                new_arr.append(elem)
                if elem == '(' and i == 0 and arr[-1] == ')':
                    continue    
                if elem == "(":
                    f += 1
            else:
                new_arr[-1] += elem
                if elem == "(":
                    f += 1            
                if elem == ")":
                    f -= 1  
        return new_arr 

    def get_priority_parentheses(arr):
        math_tokens = ['/', '*', '-', '+']
        new_arr = arr.copy()
        if new_arr[0] == '(' and new_arr[-1] == ')':
            new_arr.pop()
            new_arr.pop(0)        
        for math_token in math_tokens:
            i = len(new_arr) - 1
            while i >= 0:
                if (new_arr[i] == math_token and not (new_arr[i - 2] == '(' and new_arr[i + 2] == ')')):
                    if new_arr[i - 1] != ')':
                        new_arr.insert(i - 1, '(')
                        i += 1
                    else:
                        f = 1
                        j = i - 1
                        while f > 0:
                            j -= 1
                            if new_arr[j] == ')':
                                f += 1
                            if new_arr[j] == '(':
                                f -= 1
                        new_arr.insert(j, '(')
                        i += 1
                    if new_arr[i + 1] != '(': 
                        new_arr.insert(i + 2, ')')
                    else:
                        f = 1
                        j = i + 1
                        while f > 0:
                            j += 1
                            if new_arr[j] == '(':
                                f += 1
                            if new_arr[j] == ')':
                                f -= 1
                        new_arr.insert(j, ')')
                i -= 1 
        return new_arr    

    def get_all_list(str):
        def iter(st, n_arr):
            new_arr = merge_parentheses(get_list(st))           
            arr = get_priority_parentheses(new_arr)     
            for i, elem in enumerate(arr):
                if elem[0] == '(' and len(elem) > 1:
                    elem = iter(elem, [])               
                n_arr.append(elem)
            return n_arr
        return iter(str, [])

    def get_result_lst(str):
        lst = get_all_list(str)
        def iter(ls, n_arr):
            for elem in ls:
                if not isinstance(elem, list):
                    n_arr.append(elem)
                else:
                    iter(elem, n_arr)
            return n_arr
        return iter(lst, [])
    return get_result_lst(math_str)


class TestGetAst(unittest.TestCase):
    
    def test_get_ast(self):
        
        st = "7+3"
        self.assertEqual(get_ast(st), ['(', '7', '+', '3', ')', ])        
        
        st = "7+3/25*(5-2)"
        self.assertEqual(get_ast(st), ['(', '7', '+', '(', '(', '3', '/', '25', ')', '*', '(', '5', '-', '2', ')', ')', ')', ]) 
        
        st = "3 + 5 - 5 + 3"
        self.assertEqual(get_ast(st), ['(', '3 ', '+', '(', '(', ' 5 ', '-', ' 5 ', ')', '+', ' 3', ')', ')'])        
        
        st = "71+32/25*(5-2*89+14)/65-21"
        self.assertEqual(get_ast(st), ['(', '71', '+', '(', '(', '(', '32', '/', '25', ')', '*', '(', '(', '(', '5', '-', '(', '2', '*', '89', ')', ')', '+', '14', ')', '/', '65', ')', ')', '-', '21', ')', ')'])
        
if __name__ == '__main__':
    unittest.main()     
