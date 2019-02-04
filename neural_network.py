import unittest

class Neuron:
    def __init__(self, m, n, level_compared = 35):
        self.level_compared = level_compared
        self.arr = self.get_array(m, n)
        
    def get_array(self, m, n):     
        a = []
        for i in range(m):
            a.append([])
            for j in range(n):
                a[i].append(0)
        return a        
                
    def aktiv_function(self, file_name):
        with open(file_name, 'r') as file:
            array_of_strings = file.read().split('\n')
        i = 0
        acc = 0
        while  i < len(self.arr):
            j = 0
            while j < len(self.arr[0]):
                acc += int(array_of_strings[i][j]) * self.arr[i][j]
                j += 1      
            i += 1
        if acc >= self.level_compared:
            return 1
        else:
            return 0

class TestNeuron(unittest.TestCase):
    
    def setUp(self):
        
        self.a = Neuron(10, 10)
        self.a.arr = [
            [1,1,1,1,1,1,1,1,1,1], 
            [1,0,0,0,0,0,0,0,0,1], 
            [1,0,0,0,0,0,0,0,0,1], 
            [1,0,0,0,0,0,0,0,0,1], 
            [1,0,0,0,0,0,0,0,0,1], 
            [1,1,1,1,1,1,1,1,1,1], 
            [1,0,0,0,0,0,0,0,0,1], 
            [1,0,0,0,0,0,0,0,0,1], 
            [1,0,0,0,0,0,0,0,0,1], 
            [1,0,0,0,0,0,0,0,0,1]]
        
    def test_activ_function(self):
        
        self.assertEqual(self.a.aktiv_function('/home/igbes/python/word-files/a-true'), 1)
        self.assertEqual(self.a.aktiv_function('/home/igbes/python/word-files/a-false-1'), 0)
        
if __name__ == '__main__':
    unittest.main()       