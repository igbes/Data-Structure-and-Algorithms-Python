import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    
    def setUp(self):
        
        self.st = Stack()
        self.st.push(0)
        self.st.push(1)
        self.st.push(2)
        self.st.push(3)
        self.st.push(4)
    
    def test_push(self):
        self.assertEqual(self.st.push(5), 5)
        self.assertEqual(self.st.stack, [0, 1, 2, 3, 4, 5])
    
    def test_pop(self):
        self.assertEqual(self.st.pop(), 4)
        self.assertEqual(self.st.stack, [0, 1, 2, 3])
        
    """def test_valid_brackets_1(self):
        str1 = "(()((())()))" 
        str2 = "(()((())())" 
        self.assertEqual(valid_brackets_1(str1), "brackets valid!")
        self.assertEqual(valid_brackets_1(str2), "brackets not valid!")
    def test_count_postfix(self):
        st = "8 2 + 5 * 9 + ="
        self.assertEqual(count_postfix(st), 59)"""        
        
if __name__ == '__main__':
    unittest.main()        
