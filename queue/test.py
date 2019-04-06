import unittest
from queue import Queue
from other_tasks import Queue_with_2stack
from other_tasks import rotate_queue

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
    
    """ проверка "вращаения" очереди по кругу на N элементов: """ 
    
    def test_rotate_queue_0(self):
        rotate_queue(self.qu, 0)
        self.assertEqual(self.qu.items, [1, 2, 3, 4, 5])  
        
    def test_rotate_queue_1(self):    
        rotate_queue(self.qu, 1)
        self.assertEqual(self.qu.items, [2, 3, 4, 5, 1])
    
    def test_rotate_queue_2(self):    
        rotate_queue(self.qu, 2)
        self.assertEqual(self.qu.items, [3, 4, 5, 1, 2]) 
        
    def test_rotate_queue_len(self):
        rotate_queue(self.qu, len(self.qu.items))
        self.assertEqual(self.qu.items, [1, 2, 3, 4, 5])  
        

"""Проверка очереди, созданной из двух стеков: """  

class testQueue_with_2stack(unittest.TestCase):  
    
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
        
    """ проверка "вращаения" очереди по кругу на N элементов: """   
    
    def test_rotate_queue_0(self):
        rotate_queue(self.qu, 0)
        self.assertEqual(self.qu.items, [1, 2, 3, 4, 5])  
        
    def test_rotate_queue_1(self):    
        rotate_queue(self.qu, 1)
        self.assertEqual(self.qu.items, [2, 3, 4, 5, 1])
    
    def test_rotate_queue_2(self):    
        rotate_queue(self.qu, 2)
        self.assertEqual(self.qu.items, [3, 4, 5, 1, 2]) 
        
    def test_rotate_queue_len(self):
        rotate_queue(self.qu, len(self.qu.items))
        self.assertEqual(self.qu.items, [1, 2, 3, 4, 5])
        
if __name__ == '__main__':
    unittest.main()        