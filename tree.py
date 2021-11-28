import functools

def add_id(tree, index):
    if( len(tree) > 0):
        v = tree[0]
        def next(a,e):
            n = add_id(e, a[1])
            return (a[0] + (n[0],), n[1])
        rest = functools.reduce(next, tree[1:], ((), index + 1))
        r = (((v, index),)+rest[0],rest[1])
    else:
        r = tree
    return r

t = ('a', ('b'), ('c', ('d'), ('e')))
print(t)
print(add_id(t, 0))