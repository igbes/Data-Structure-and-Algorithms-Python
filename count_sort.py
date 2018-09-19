import unittest

def ksort(ls, l):
    
    """Сортировка списка строк за линейное время с применением
    хэш-функции"""
    
    def get_hash(st):
        sum_st = ord(st[0]) + int(st[1]) + int(st[2])
        return sum_st % l
    
    def count():
        ls_lst = [[] for i in range(l)]
        for i in ls:
            ls_lst[get_hash(i)].append(i)
        return ls_lst
    return count()


class TestCountSort(unittest.TestCase):
    
    def test_ksort(self):
                
        lst = ['f16', 'h62', 'h54', 'c19', 'b12', 'h44', 'c72', 'g32', 'e75', 'e37', 'h45', 'b11', 'd38', 'e26', 'a42']
        self.assertEqual(ksort(lst, 20), 
                         [['b11'], ['b12'], [], ['a42'], [], [], [], [], ['c72', 'g32'], ['f16', 'c19', 'e26'], [], ['e37', 'd38'], ['h62', 'h44'], ['h54', 'e75', 'h45'], [], [], [], [], [], []])
        
if __name__ == '__main__':
    unittest.main()      