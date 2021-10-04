class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror(node):
    if node == None:
        return
    else:
        ## Important Recursive Calls
        mirror(node.left)
        mirror(node.right)
        node.left, node.right = node.right, node.left
    
def inOrder(node):
    if node == None:
        return
    
    inOrder(node.left)
    print(node.data, end= " ")
    inOrder(node.right)

## Driver Code
if __name__ =="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder Traversal of Original Binary Tree:")
    inOrder(root)

    mirror(root)

    print("\nInorder Traversal of Mirror Binary Tree:")
    inOrder(root)