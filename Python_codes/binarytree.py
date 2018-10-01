
c = 0

class node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inorder(temp):
        if temp is None:
            return

        inorder(temp.left)
        print(temp.data)
        inorder(temp.right)

def insert(root, newnode):
    if root is None:
        root = newnode
    else:
        if root.data < newnode.data:
            if root.right is None:
                root.right = newnode
            else:
                insert(root.right, newnode)
        else:
            if root.left is None:
                root.left = newnode
            else:
                insert(root.left, newnode)


def search(root, key):
    if root is None:
        print("Not found")
        return

    if root.data == key:
        return root
    else:
        if root.data < key:
            return search(root.right,key)
        else:
            return search(root.left,key)

def findmin(root):
    if root is None:
        return

    while root.left is not None:
        root = root.left

    return root

def findmax(root):
    if root is None:
        return

    while root.right is not None:
        root = root.right

    return root

def kthlargestelement(root, k):
    global c
    if root is None:
        return

    #print(c)
    kthlargestelement(root.right, k)
    c = c+1
    if c == k:
        print(root.data)
        return
    
    kthlargestelement(root.left, k)

    

def deletenode(root,key):
    if root.data < key:
        deletenode(root.right, key)

    elif root.data > key:
        deletenode(root.left, key)

    else:
        if root.left is None and root.right is None:
            root = None
        elif root.left is None:
            temp = root.right
            root.right = None
            root.data = temp.data
        elif root.right is None:
            temp = root.left
            root.left = None
            root.data = temp.data
        else:
            current = root.left
            while current.left is not None:
                current = current.left

            root.data = current.data
            current = None
                
        



root = node(5)
e1 = node(2)
insert(root, e1)
e2 = node(3)
insert(root, e2)
e3 = node(7)
insert(root, e3)
e4 = node(8)
insert(root, e4)
inorder(root)

#inorder(search(root,2))
        
#deletenode(root, 5)
#inorder(root)
#min = findmin(root)
#print(min.data)
#max = findmax(root)
#print(max.data)
kthlargestelement(root, 2)
