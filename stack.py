import unittest
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
class Stack_reverse:
    # стек, вершина которого - начало списка
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        return self.stack.insert(0)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[0]

    def size(self):
        return len(self.stack) 
    
def valid_brackets(item):
    # проверка сбалансированности скоабок (без стека)
    f = 0
    for i in range(len(item)):
        if item[i] == '(':
            f += 1
        else:
            f -= 1
        if f < 0:
            return print("brackets not valid!")
    if f == 0:
        return print("brackets valid!")
    else:
        return print("brackets not valid!")
    
def valid_brackets_1(item):
    # проверка сбалансированности скобок (со стеком)
    stk = Stack()
    def iter_in_stack(i):
        if i < 0:
            return
        stk.push(item[i])
        return iter_in_stack(i - 1)
    iter_in_stack(len(item) - 1)
    
    def iter(f, size):
        if size == 0:
            if f == 0: 
                return "brackets valid!"
            else: 
                return "brackets not valid!"
        if stk.pop() == '(': 
            return iter(f + 1, size - 1)
        else:
            return iter(f - 1, size - 1)
        if f < 0:
            return "brackets not valid!"
        return iter(f, size - 1)
    return iter(0, stk.size())
    
def count_postfix(item):
    # реализация посфиксной нотации вычислений
    stk_1 = Stack()
    stk_2 = Stack()
    def iter_in_stack(i):
        if i < 0:
            return 
        if item[i] == " ":
            return iter_in_stack(i - 1)
        stk_1.push(item[i])
        return iter_in_stack(i - 1)
    iter_in_stack(len(item) - 1)
    
    while True:
        itm = (stk_1.pop())
        if itm == '=': 
            result = stk_2.peak()
            return result
        if itm.isdigit():
            stk_2.push(int(itm))
            continue
        else:
            num1 = stk_2.pop()
            num2 = stk_2.pop()
            if itm == '+': res = num2 + num1
            elif itm == '-': res = num2 - num1
            elif itm == '*': res = num2 * num1
            else: res = num2 / num1
            stk_2.push(res)
            
class TestStack(unittest.TestCase):
    
    def test_valid_brackets_1(self):
        str1 = "(()((())()))" 
        str2 = "(()((())())" 
        self.assertEqual(valid_brackets_1(str1), "brackets valid!")
        self.assertEqual(valid_brackets_1(str2), "brackets not valid!")
    def test_count_postfix(self):
        st = "8 2 + 5 * 9 + ="
        self.assertEqual(count_postfix(st), 59)        
        
if __name__ == '__main__':
    unittest.main()        
   