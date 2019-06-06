
import unittest
from generate_BBSTArray import GenerateBBSTArray

class TestGenerateBBSTArray(unittest.TestCase):
    
    def setUp(self):
        pass
            
    def test_GenerateBBSTArray(self):
        
        self.assertEqual(GenerateBBSTArray([7]), [7])
        
        self.assertEqual(GenerateBBSTArray([1, 2, 3]), [2, 1, 3])
        
        self.assertEqual(GenerateBBSTArray([7, 5, 6, 4, 2, 3, 1]), [4, 2, 6, 1, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()  
