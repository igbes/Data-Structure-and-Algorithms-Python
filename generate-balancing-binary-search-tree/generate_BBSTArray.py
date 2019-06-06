def GenerateBBSTArray(a):
    arr = a[:]
    arr.sort()    
    
    def get_depth(length):
        """Возвращает глубину дерева, принимает параметром
        длину списка"""
        depth = 0
        number_in_level = 1
        total = 1
        while total < length:
            number_in_level *= 2
            total += number_in_level
            depth += 1
        return depth
    
    def get_index(val_1, val_2):
        if (val_2 + val_1) % 2 == 0:
            index = (val_2 + val_1) / 2
        elif (val_2 + val_1) % 2 != 0:
            index = (val_2 + val_1 + 1) / 2            
        return int(index)
    
    depth = get_depth(len(arr) - 1)
    res_arr = [list() for elem in range(depth + 1)]
       
    def iter(left_index, right_index, level):
        node_index = get_index(left_index, right_index)
        if node_index > len(arr) - 1:
            return        
        res_arr[level].append(arr[node_index])
        if right_index - left_index == 0:
            return 
        iter(left_index, node_index - 1, level + 1)
        iter(node_index + 1, right_index, level + 1)
    
    iter(0, len(arr) - 1, 0)
    
    def get_BBSTArray(lst):
        res = []
        for element in lst:
            res = res + element
        return res
    return get_BBSTArray(res_arr)
