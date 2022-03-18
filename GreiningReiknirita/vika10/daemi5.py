def fall1(root, x):
    fall2(root, x-1)

def fall2(root, x):
    if x==NULL: return NULL
    if size(root.left) > x: return fall2(root.left, x)
    elif size(root.left) < x: return fall2(root.right, x - size(root.left) - 1)
    else: return root

