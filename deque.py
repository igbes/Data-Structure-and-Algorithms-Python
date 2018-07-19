import unittest
class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0,item)

    def removeFront(self):
        return self.queue.pop()

    def removeTail(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    
def is_palindrome(item):
    i = len(item) // 2 - 1
    if len(item) % 2 == 0:
        j = i + 1
    else:
        j = i + 2
    while i >= 0:
        if item[i] != item[j]:
            return "not palindrome"
        i -= 1
        j += 1
    return "palindrome"     

def is_palindrome_1(item):
    deque = Deque()
    for i in range(len(item)):
        deque.addTail(item[i])
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return "not palindrome"
    return "palindrome"    
        
class TestQueue(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome_1("level"), "palindrome")
        self.assertEqual(is_palindrome_1("lever"), "not palindrome")    
        
    def test_is_palindrome_1(self):
        self.assertEqual(is_palindrome_1("level"), "palindrome")
        self.assertEqual(is_palindrome_1("lever"), "not palindrome")
        
if __name__ == '__main__':
    unittest.main()        