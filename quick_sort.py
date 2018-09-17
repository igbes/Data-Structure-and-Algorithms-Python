import unittest, time, copy, random, shell_sort

def quick_sort(M):
    
    def split_array(N, i1, i2):
        limit_1 = i1
        limit_2 = i2
        
        while True:
            if i1 == i2:
                return [i1, i2]
            if M[i1] == N and M[i2] == N:
                if i1 == i2 - 1:
                    return [i1, i2] 
                
                i1_step = 1
                while M[i1 + i1_step] == N:
                    i1_step += 1
                    if i1 + i1_step == i2:
                        if i2 < limit_2:
                            i2 += 1 
                        if i1 > limit_1:    
                            i1 -= 1 
                        return [i1, i2] 
                    
                i2_step = 1
                while M[i2 - i2_step] == N : 
                    i2_step += 1 
                    if i1 == i2 - i2_step:
                        if i2 < limit_2:
                            i2 += 1 
                        if i1 > limit_1:    
                            i1 -= 1                       
                        return [i1, i2]
                    
                if M[i1 + i1_step] > N:
                    M[i2], M[i1 + i1_step] = M[i1 + i1_step], M[i2]
                if M[i1 + i1_step] < N:
                    M[i1], M[i1 + i1_step] = M[i1 + i1_step], M[i1]    
                                 
                if M[i2 - i2_step] < N:
                    M[i1], M[i2 - i2_step] = M[i2 - i2_step], M[i1]
                if M[i2 - i2_step] > N:
                    M[i2], M[i2 - i2_step] = M[i2 - i2_step], M[i2]     
                    
            while M[i1] < N:
                if i1 == i2 - 1:
                    if i2 < limit_2:
                        i2 += 1 
                    return [i1, i2] 
                i1 += 1
                
            while M[i2] > N:
                if i1 == i2 - 1:
                    if i1 > limit_1:
                        i1 -= 1 
                    return [i1, i2]            
                i2 -= 1          
                
            M[i1], M[i2] = M[i2], M[i1]
           
        return [i1, i2]     

    def result(m1, m2):
        if m1 == m2:
            return         
        a = split_array(M[m1], m1, m2)
        left = m1
        right = m2
        result(left, a[0])
        result(a[1], right)
    return result(0, len(M) - 1)



ls = [random.randint(0, 30000) for i in range(30000)]#lst = copy.copy(ls)
lst = copy.copy(ls)

start_time = time.time() 
quick_sort(ls)
print("Q_sort => %s seconds" % (time.time() - start_time))

start_time = time.time() 
shell_sort.shell_sort(lst)
print("shell_sort => %s seconds" % (time.time() - start_time))


class TestSplitArray(unittest.TestCase):
    
    def test_split_array(self):
       
        
        ls = [3, 0, 1, 4]
        quick_sort(ls)
        self.assertEqual(ls, [0, 1, 3, 4])
        
        
        ls = [4, 3, 0, 1]
        quick_sort(ls)
        self.assertEqual(ls, [0, 1, 3, 4])
        
        ls = [30, 20, 10, 4]
        quick_sort(ls)
        self.assertEqual(ls, [4, 10, 20, 30])
        
        
        ls = [4, 30, 20, 10]
        quick_sort(ls)
        self.assertEqual(ls, [4, 10, 20, 30])
        
        ls = [4, 3, 4, 3, 4, 3]
        quick_sort(ls)
        self.assertEqual(ls, [3, 3, 3, 4, 4, 4])
        
        ls = [9]
        quick_sort(ls)
        self.assertEqual(ls, [9])
        
        ls = [9, 9]
        quick_sort(ls)
        self.assertEqual(ls, [9, 9])
        
        ls = [27, -6, 4, 8, -9, 53, 2, 4, 0, -1, 15, 4, 25, 0, 4]
        quick_sort(ls)
        self.assertEqual(ls, [-9, -6, -1, 0, 0, 2, 4, 4, 4, 4, 8, 15, 25, 27, 53])
        
if __name__ == '__main__':
    unittest.main()      
