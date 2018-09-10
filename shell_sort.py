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
    
    def sequence_knut():
        """ Возвращает интервальную последовательность Кнута 
        для заданного списка lst """
        
        l = []
        n = 1
        while n <= len(lst):
            l.insert(0, n)
            n = 3 * n + 1        
        return l
                
    def result_sort():
        for i in sequence_knut():
            insert_sort_step(i)
        return lst
    
    return result_sort()


class TestShellSort(unittest.TestCase):
    
    def test_insertion_sort_step_1(self):
        """
        Проверка сортировки Шелла:
        """
        ls = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(shell_sort(ls), [1, 2, 3, 4, 5, 6, 7])
        
        ls = [7, 6, 4, 8, 9, 3, 2, 10, 5, 1, 15, 13, 14, 12, 11]
        self.assertEqual(shell_sort(ls), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        
if __name__ == '__main__':
    unittest.main()      
