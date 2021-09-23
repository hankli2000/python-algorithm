class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def printInorder(root):
	'''inorder (left, root, right) '''
	if root:
		printInorder(root.left)
		print(root.val)
		print(root.right)


def printPostOrder(root):
	'''postorder (left, right, root)'''
	if root:
		printPostOrder(root.left)
		printPostOrder(root.right)
		print(root.val)

def printPreOrder(root):
	'''preorder (root, left, right) '''
	if root:
		print(root.val)
		printPreOrder(root.left)
		printPreOrder(root.right)

def printLeverOrder(root):
	'''BFS, print all nodes in one lever, then go to next level  '''
	if root:
		q = deque()
		q.append(root)
		if q:
			n = q.popleft()
			print(n.val)
			q.append(n.left)
			q.append(n.right)

def printOneLevelNodes(root, level):
	if root is None: 
		return
	if level ==1:
		print(root.val, end=' ')
	elif level > 1:
		printOneLevelNodes(root.left, level - 1)
		printOneLevelNodes(root.right, level - 1)


def height(root):
	if root is None:
		return 0
	lheight = height(root.left)
	rheight = height(root.right)
	height = max(lheight, rheight) + 1



# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Preorder traversal of binary tree is"
printPreorder(root)
 
print "\nInorder traversal of binary tree is"
printInorder(root)
 
print "\nPostorder traversal of binary tree is"
printPostorder(root)
