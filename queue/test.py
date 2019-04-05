import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    
    def setUp(self):
        self.qu = Queue()
        self.qu.enqueue(1)
        self.qu.enqueue(2)
        self.qu.enqueue(3)
        self.qu.enqueue(4)
        self.qu.enqueue(5)        
                
    def test_enqueue(self):
        self.qu.enqueue(6)
        self.assertEqual(self.qu.items, [1, 2, 3, 4, 5, 6])
        
    def test_dequeue(self):
        self.qu.dequeue()
        self.assertEqual(self.qu.items, [2, 3, 4, 5])    
           
if __name__ == '__main__':
    unittest.main()        