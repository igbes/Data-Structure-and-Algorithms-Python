
import unittest
from deque import Deque
from other_tasks import is_palindrome

class TestQueue(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_addFront(self):
        self.deque = Deque()
        self.deque.addFront(0)
        self.deque.addFront(1)
        self.deque.addFront(2)
        self.assertEqual(self.deque.items, [2, 1, 0])    
    
    def test_addTail(self):
        self.deque = Deque()
        self.deque.addTail(0)
        self.deque.addTail(1)
        self.deque.addTail(2)
        self.assertEqual(self.deque.items, [0, 1, 2])
    
    def test_removeFront(self):
        self.deque = Deque()
        self.deque.addFront(0)
        self.deque.addFront(1)
        self.deque.addFront(2)        
        self.assertEqual(self.deque.items, [2, 1, 0]) 
        self.deque.removeFront()
        self.assertEqual(self.deque.items, [1, 0])
        
    def test_removeTail(self):
        self.deque = Deque()
        self.deque.addTail(0)
        self.deque.addTail(1)
        self.deque.addTail(2)
        self.assertEqual(self.deque.items, [0, 1, 2])
        self.deque.removeTail()
        self.assertEqual(self.deque.items, [0, 1])  
        
    def test_size(self):
        self.deque = Deque()
        self.assertEqual(self.deque.size(), 0)
        self.deque.addTail(0)
        self.deque.addTail(1)
        self.assertEqual(self.deque.size(), 2)
        
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("level"), True)
        self.assertEqual(is_palindrome("lever"), False)        
    
if __name__ == '__main__':
    unittest.main()        