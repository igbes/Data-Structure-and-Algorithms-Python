import unittest
from bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    
    def setUp(self):
        self.my_filter = BloomFilter(32)
        self.my_filter.add("0123456789")
        self.my_filter.add("1234567890")
        self.my_filter.add("2345678901")
        self.my_filter.add("3456789012")
        self.my_filter.add("4567890123")
        self.my_filter.add("5678901234")
        self.my_filter.add("6789012345")
        self.my_filter.add("7890123456")
        self.my_filter.add("8901234567")
        self.my_filter.add("9012345678")
    
    def test_is_value(self):
        self.assertEqual(self.my_filter.is_value("0123456789"), True)
        self.assertEqual(self.my_filter.is_value("3456789012"), True) 
        self.assertEqual(self.my_filter.is_value("1111111111"), False) 
        self.assertEqual(self.my_filter.is_value("2222222222"), False)
   
if __name__ == '__main__':
    unittest.main()        