import unittest
import hashlib
import datetime
import time

class Block:
    
    def __init__(self, prev_hash, current_hash, index, time, data, nonce):
        
        self.prev_hash = prev_hash
        self.current_hash = current_hash
        self.index = index
        self.time = time
        self.data = data
        self.nonce = nonce
    
class Blockchain:
    
    def __init__(self, number_zero = 1):
        
        self.blockchain = []
        self.number_zero = number_zero
        
    def get_hash(self, prev_hash, data, time, index):
        
        byte_str = data.encode()
        nonce = 0
        new_data = '{0}{1}{2}{3}{4}'.format(prev_hash, data, time, str(index), str(nonce))
        byte_str = new_data.encode()
        str_hash = hashlib.md5(byte_str).hexdigest()
        while str_hash[-self.number_zero:] != '0' * self.number_zero:
            nonce+=1
            new_data = '{0}{1}{2}{3}{4}'.format(prev_hash, data, time, str(index), str(nonce))
            byte_str = new_data.encode()
            str_hash = hashlib.md5(byte_str).hexdigest()
        return [str_hash, nonce]   

    def add_block(self, data):
        
        time = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        if len(self.blockchain) == 0:
            prev_hash = '0000'
            index = 0
        else:
            prev_hash = self.blockchain[-1].current_hash
            index = len(self.blockchain)
        [current_hash, nonce] = self.get_hash(prev_hash, data, time, index)
        self.blockchain.append(Block(prev_hash, current_hash, index, time, data, nonce))
        
    def get_block(self, str_hash):
        
        for block in self.blockchain:
            if block.current_hash == str_hash:
                return block.index
        return False  
    
    def check_chain(self):
        
        for block in self.blockchain:
            [calculated_hash, nonce] = self.get_hash(block.prev_hash, block.data, block.time, block.index)
            if block.current_hash != calculated_hash:
                return 'block {0} is fail!'.format(block.index)
        return 'blockchain is true'

class TestBlockchain(unittest.TestCase):
    
    def setUp(self):
        
        self.chain = Blockchain(3)       
        self.chain.add_block('Питон')
        self.chain.add_block('Python')
        self.chain.add_block('Джаваскрипт')
        self.chain.add_block('Javascript')
        
    def test_get_hash(self):
        
        self.assertEqual(self.chain.get_hash('bdfa8a30d765d9a0f6e4e2fdad051000', 'Javascript', 20190126161749, 3), ['b487df276ef3680cec3ae021f42fc000', 6394])
        
    def test_get_block(self):
        
        current = self.chain.blockchain[1]
        self.assertEqual(self.chain.get_block(current.current_hash), 1)
        
    def test_check_chain(self): 
        
        self.assertEqual(self.chain.check_chain(), 'blockchain is true')
        self.chain.blockchain[2].prev_hash = 123456789
        self.assertEqual(self.chain.check_chain(), 'block {0} is fail!'.format(self.chain.blockchain[2].index))
       
if __name__ == '__main__':
    unittest.main()       
