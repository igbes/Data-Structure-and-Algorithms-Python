import unittest

class Neuron:
    def __init__(self, m, n, level_compared = 31):
        self.m = m
        self.n = n
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
        if acc > self.level_compared:
            return 1
        else:
            return 0
        
    def learn_network(self, file_name, flag = False):
        with open(file_name, 'r') as file:
            array_of_strings = file.read().split('\n')        
        
        for i in range(self.m):
            for j in range(self.n):
                if flag == True and int(array_of_strings[i][j]) == 1 and self.arr[i][j] == 0:
                    self.arr[i][j] = 1
                if flag == False and int(array_of_strings[i][j]) == 1 and self.arr[i][j] == 0:
                    self.arr[i][j] = -1

class TestNeuron(unittest.TestCase):
    
    def setUp(self):
        self.a = Neuron(10, 10)
        self.a.learn_network('./word-files/a-1', True)
        self.a.learn_network('./word-files/a-2', True)
        self.a.learn_network('./word-files/a-3', True)
        self.a.learn_network('./word-files/a-4', True)
        self.a.learn_network('./word-files/a-5', True)
        self.a.learn_network('./word-files/a-6', True)
        self.a.learn_network('./word-files/a-7', True)
        self.a.learn_network('./word-files/a-8', True)
        self.a.learn_network('./word-files/a-9', True)
        self.a.learn_network('./word-files/a-10', True)
        
        
    def test_learn_network_b(self):
        self.a.learn_network('./word-files/b', False)
        self.assertEqual(self.a.aktiv_function('./word-files/b'), 0)        
    def test_learn_network_c(self):
        self.a.learn_network('./word-files/b', False)
        self.assertEqual(self.a.aktiv_function('./word-files/c'), 0)  
    
    def test_learn_network_f(self):
        self.a.learn_network('./word-files/f', False)
        self.assertEqual(self.a.aktiv_function('./word-files/f'), 0) 
        
        
    def test_learn_network_h(self):
        self.a.learn_network('./word-files/h', False)
        self.assertEqual(self.a.aktiv_function('./word-files/h'), 0)         
    def test_learn_network_k(self):
        self.a.learn_network('./word-files/k', False)
        self.assertEqual(self.a.aktiv_function('./word-files/k'), 0) 
        
    def test_learn_network_l(self):
        self.a.learn_network('./word-files/l', False)
        self.assertEqual(self.a.aktiv_function('./word-files/l'), 0)  
        
    def test_learn_network_m(self):
        self.a.learn_network('./word-files/m', False)
        self.assertEqual(self.a.aktiv_function('./word-files/m'), 0)
        
    def test_learn_network_n(self):
        self.a.learn_network('./word-files/n', False)
        self.assertEqual(self.a.aktiv_function('./word-files/n'), 0)
        
    def test_learn_network_o(self):
        self.a.learn_network('./word-files/o', False)
        self.assertEqual(self.a.aktiv_function('./word-files/o'), 0) 
        
    def test_learn_network_p(self):
        self.a.learn_network('./word-files/p', False)
        self.assertEqual(self.a.aktiv_function('./word-files/p'), 1) # error 
        
    def test_learn_network_r(self):
        self.a.learn_network('./word-files/r', False)
        self.assertEqual(self.a.aktiv_function('./word-files/r'), 1) # error         
        
    
    
    def test_learn_network_a(self):
        self.assertEqual(self.a.aktiv_function('./word-files/a-1'), 1)  
        self.assertEqual(self.a.aktiv_function('./word-files/a-2'), 0) # error
        self.assertEqual(self.a.aktiv_function('./word-files/a-3'), 0) # error
        self.assertEqual(self.a.aktiv_function('./word-files/a-4'), 0) # error
        self.assertEqual(self.a.aktiv_function('./word-files/a-5'), 1) 
        self.assertEqual(self.a.aktiv_function('./word-files/a-6'), 1) 
        self.assertEqual(self.a.aktiv_function('./word-files/a-7'), 0) # error
        self.assertEqual(self.a.aktiv_function('./word-files/a-8'), 1) 
        self.assertEqual(self.a.aktiv_function('./word-files/a-9'), 1) 
        self.assertEqual(self.a.aktiv_function('./word-files/a-10'), 0) # error
    
if __name__ == '__main__':
    unittest.main()       
   
  
