import unittest

def shell_sort(lst):
    
    def insert_sort_step(step):
        for index in range(len(lst)):
            for i in range(step + index, len(lst), step):
                j = i 
                while j >= step:
                    if lst[j] < lst[j - step]:
                        lst[j], lst[j - step] = lst[j - step], lst[j]
                        j -= step
                    else:
                        break
                if j + step >= len(lst):
                    return lst 
                
    def result_sort(gap):
        while gap:
            insert_sort_step(gap)
            gap //= 2
        return lst
    
    return result_sort(len(lst) // 2)  


class TestShellSort(unittest.TestCase):
    
    def test_insertion_sort_step_1(self):
        """
        Проверка сортировки Шелла:
        """
        ls = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(shell_sort(ls), [1, 2, 3, 4, 5, 6, 7])
        
        ls = [7, 6, 4, 8, 9, 3, 2, 10, 5, 1]
        self.assertEqual(shell_sort(ls), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
if __name__ == '__main__':
    unittest.main()      
