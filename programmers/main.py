def pre(root) :
    if root == '.':
        return
    print(root,end='')
    pre(tree[root][0])
    pre(tree[root][1])

n = int(input())
tree = {}

for i in range(n):
    root,left,right = input().split()
    tree[root] = (left,right)

print(preorder('A'))