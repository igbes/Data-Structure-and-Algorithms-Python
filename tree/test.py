import unittest
from tree import SimpleTreeNode
from tree import SimpleTree


class TestSimpleTree(unittest.TestCase):
    
    def setUp(self):
        
        self.tree = SimpleTree(SimpleTreeNode(10, None))
        self.tree.AddChild(self.tree.current, SimpleTreeNode(5, None))
        self.tree.AddChild(self.tree.current, SimpleTreeNode(7, None))
        self.tree.AddChild(self.tree.current, SimpleTreeNode(8, None))
        self.tree.current = self.tree.current.Children[0]
        self.tree.AddChild(self.tree.current, SimpleTreeNode(12, None))
        self.tree.AddChild(self.tree.current, SimpleTreeNode(37, None))
        
    def test_add_child(self):
        self.assertEqual([node.NodeValue for node in self.tree.GetAllNodes()], [10, 5, 12, 37, 7, 8]) 
        self.tree.current = self.tree.current.Parent.Children[1]
        self.tree.AddChild(self.tree.current, SimpleTreeNode(100, None))
        self.assertEqual([node.NodeValue for node in self.tree.GetAllNodes()], [10, 5, 12, 37, 7, 100, 8])  
        #self.assertEqual(self.tree.node_number, 7)
        #self.assertEqual(self.tree.leaf_number, 4)
    
    def test_DeleteNode(self):
        self.assertEqual(self.tree.current.NodeValue, 5)
        self.assertEqual([node.NodeValue for node in self.tree.GetAllNodes()], [10, 5, 12, 37, 7, 8])
        
        self.tree.DeleteNode(self.tree.current)
        self.assertEqual([node.NodeValue for node in self.tree.GetAllNodes()], [10, 7, 8, 12, 37])  
       
    
    def test_GetAllNodes(self):
        self.assertEqual([node.NodeValue for node in self.tree.GetAllNodes()], [10, 5, 12, 37, 7, 8]) 
        self.tree.AddChild(self.tree.current, SimpleTreeNode(100, None))
        
    def test_FindNodesByValue(self):
        self.assertEqual([node.NodeValue for node in self.tree.FindNodesByValue(7)], [7]) 
        
        self.tree.AddChild(self.tree.current, SimpleTreeNode(7, None))
        self.assertEqual([node.NodeValue for node in self.tree.FindNodesByValue(7)], [7, 7]) 
        
    def test_MoveNode(self):
        self.assertEqual([node.NodeValue for node in self.tree.GetAllNodes()], [10, 5, 12, 37, 7, 8]) 
        self.assertEqual(self.tree.current.NodeValue, 5) 
        
        self.tree.MoveNode(self.tree.current, self.tree.root.Children[-1])
        self.assertEqual([node.NodeValue for node in self.tree.GetAllNodes()], [10, 7, 8, 5, 12, 37])
        
    def test_Count(self):
        self.assertEqual(self.tree.Count(), 7)
        
    def test_LeafCount(self):
        self.assertEqual(self.tree.LeafCount(), 4)  
        
    def test_LevelCount(self):
        self.assertEqual(self.tree.LevelCount(self.tree.root), 0)
        
        self.assertEqual(self.tree.current.NodeValue, 5)
        self.assertEqual(self.tree.LevelCount(self.tree.current), 1)
            
if __name__ == '__main__':
    unittest.main()  